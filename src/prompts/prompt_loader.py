from jinja2 import Environment, FileSystemLoader, select_autoescape
from schemas import tool_catalog
from configs import PROMPTS_PATH

_env = Environment(
    loader=FileSystemLoader(PROMPTS_PATH),
    trim_blocks=True,
    lstrip_blocks=True,
    autoescape=select_autoescape(),
)

def render_template(name: str, **context) -> str:
    return _env.get_template(name).render(**context)

def build_system_prompt(
    *,
    extra_guidance: str = "",
) -> str:

    return render_template(
        "system_prompt.jinja",
        tools=tool_catalog(),
        extra_guidance=extra_guidance,
    )