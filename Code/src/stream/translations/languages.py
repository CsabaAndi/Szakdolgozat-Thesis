import yaml
import streamlit as st
from pathlib import Path


@st.fragment
def load_translations(language_code):
    language_file = Path.cwd() / f"stream/translations/i18n/{language_code}.yaml"

    try:
        with open(language_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        st.error(f"Translation file for '{language_code}' not found.")
    except yaml.YAMLError as e:
        st.error(f"YAML parsing error: {e}")
    return {}


def translate(key):
    translations = load_translations(st.session_state.selected_language)
    return translations.get(key, key)
