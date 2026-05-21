from __future__ import annotations

import os
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

import frontmatter
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = PROJECT_ROOT / "dist"
CONTENT_DIR = PROJECT_ROOT / "content"
PROJECTS_DIR = CONTENT_DIR / "projects"
TEMPLATE_DIR = PROJECT_ROOT / "templates"
STATIC_DIR = PROJECT_ROOT / "static"

markdown_renderer = markdown.Markdown(
    extensions=["extra", "toc", "sane_lists"],
    output_format="html5",
)


def normalize_base_path(value: str) -> str:
    value = value.strip().strip("/")
    return f"/{value}" if value else ""


def prefixed_path(path: str, base_path: str) -> str:
    if not path.startswith("/"):
        return path
    return f"{base_path}{path}" if base_path else path


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data or {}


def render_markdown(text: str) -> str:
    markdown_renderer.reset()
    return markdown_renderer.convert(text)


def load_profile() -> dict[str, Any]:
    return load_yaml(CONTENT_DIR / "profile.yaml")


def load_projects() -> list[dict[str, Any]]:
    projects: list[dict[str, Any]] = []
    for path in sorted(PROJECTS_DIR.glob("*.md")):
        post = frontmatter.load(path)
        metadata = dict(post.metadata)
        metadata["slug"] = path.stem
        metadata["body"] = render_markdown(post.content)
        projects.append(metadata)
    return sorted(projects, key=lambda project: project.get("order", 99))


def url_for_static_export(base_path: str):
    def url_for(name: str, **params: Any) -> str:
        if name == "static":
            path = params.get("path", "")
            return f"{base_path}/static{path}" if base_path else f"/static{path}"
        if name == "index":
            return f"{base_path}/" if base_path else "/"
        if name == "project_detail":
            slug = params["slug"]
            return f"{base_path}/projects/{slug}/" if base_path else f"/projects/{slug}/"
        raise ValueError(f"Unsupported route for static export: {name}")

    return url_for


def profile_for_export(base_path: str) -> dict[str, Any]:
    profile = deepcopy(load_profile())
    person = profile.get("person", {})
    for key in ("cv_path", "photo_path"):
        if key in person:
            person[key] = prefixed_path(person[key], base_path)
    return profile


def build_static_site(output_dir: Path = DIST_DIR, base_path: str = "") -> Path:
    base_path = normalize_base_path(base_path)
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    shutil.copytree(STATIC_DIR, output_dir / "static")
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.globals["url_for"] = url_for_static_export(base_path)

    profile = profile_for_export(base_path)
    projects = load_projects()

    index_html = env.get_template("index.html").render(
        profile=profile,
        projects=projects,
        page_title=profile["site"]["title"],
    )
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    project_template = env.get_template("project_detail.html")
    for project in projects:
        project_dir = output_dir / "projects" / project["slug"]
        project_dir.mkdir(parents=True)
        html = project_template.render(
            profile=profile,
            project=project,
            projects=projects,
            page_title=f"{project['title']} | {profile['site']['title']}",
        )
        (project_dir / "index.html").write_text(html, encoding="utf-8")

    return output_dir


if __name__ == "__main__":
    site_base_path = os.environ.get("SITE_BASE_PATH", "")
    output = build_static_site(base_path=site_base_path)
    print(f"Static site exported to {output}")
