import os


def get_settings_module():
    """Choose local vs deployment Django settings."""
    env = str(os.getenv("DJANGO_ENV", "")).strip().lower()
    use_deploy = str(os.getenv("USE_DEPLOYMENT_SETTINGS", "")).strip().lower()

    is_production_env = env in {"prod", "production", "live"}
    is_deploy_flag = use_deploy in {"1", "true", "yes", "on"}
    is_render = "RENDER_EXTERNAL_HOSTNAME" in os.environ

    if is_production_env or is_deploy_flag or is_render:
        return "BackEnd.deployment_settings"
    return "BackEnd.settings"

