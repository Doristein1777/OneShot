import streamlit as st
from core.GoogleSheetPublic import fetch_data
from core.OpenAI import llm_run
import pyperclip


def create_save_to_clipboard(button_key, state_key):
    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write(
            "Before ending your session, ensure you've saved all necessary information. Use the button below to copy the above refined output fields to your clipboard."
        )
    with right_column:
        if st.button("Save to Clipboard", key=button_key, use_container_width=True):
            pyperclip.copy(st.session_state[state_key])


def main():
    # Define the custom CSS
    custom_css = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
            
            body {
                font-family: 'Open Sans', sans-serif;
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Poppins', sans-serif;
            }
        </style>
    """

    # Inject custom CSS into the Streamlit app
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("Google Sheet Data")

    data = fetch_data()

    st.write(
        """Navigating the complexities of grant applications requires a robust and informed knowledge base about the company in question. This dedicated platform empowers consultants to craft a nuanced, detailed, and tailored profile of the company, laying the foundation for effectively answering every grant-related query. From understanding the company's core product or service to articulating its mission and vision, this tool harnesses advanced AI capabilities to streamline and enhance the content creation process.\n\nYour confidentiality is paramount. Please be assured that the integrity and privacy of your information are upheld to the highest standard. This session operates in a secure environment where no external entity, be it our team at GrowthGarner or the AI providers, has access to the data you input. However, do bear in mind that upon closing this session, unsaved data will be irretrievably lost. We urge you to diligently save and backup your progress.\n\nPlease Note: This session is private and secure. No third party, including our team at GrowthGarner and the AI providers, can access the information you input here.\n\nEnsure you save your progress regularly. Once this session is closed, any unsaved information will be lost permanently.\n\nEmbark on this collaborative journey between human expertise and AI efficiency to craft compelling narratives that resonate with grant evaluators."""
    )

    # Text Input Area
    input_string = st.text_area(
        "Initial Text or Notes",
        key="text_area_0",
        placeholder="Enter any available text bout the company. This could be excerpts from their website, notes from meetings, or any other relevant material that can serve as a foundation for the knowledge base.",
    )
    left_column, right_column = st.columns([5, 1])

    if "product_overview" not in st.session_state:
        st.session_state.product_overview = ""

    with left_column:
        st.write(data[0]["button_label"])
    with right_column:
        if st.button("Generate", key="btn_generate_1", use_container_width=True):
            st.session_state.product_overview = llm_run(
                model=data[0]["model"],
                temperature=data[0]["temperature"],
                template=data[0]["prompt"],
                input_string=input_string,
            )

    st.session_state.product_overview = st.text_area(
        "product_overview",
        label_visibility="collapsed",
        key="text_area_1",
        value=st.session_state.get("product_overview", ""),
    )

    create_save_to_clipboard(f"copy_btn_1", data[0]["name"])

    if "vision_mission" not in st.session_state:
        st.session_state.vision_mission = ""

    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write(data[1]["button_label"])
    with right_column:
        if st.button("Generate", key="btn_generate_2", use_container_width=True):
            st.session_state.vision_mission = llm_run(
                model=data[1]["model"],
                temperature=data[1]["temperature"],
                template=data[1]["prompt"],
                **{
                    k: st.session_state.get(k, "")
                    for k in data[1]["input_params"].split(",")
                },
            )

    st.session_state.vision_mission = st.text_area(
        "vision_mission",
        label_visibility="collapsed",
        key="text_area_2",
        value=st.session_state.get("vision_mission", ""),
    )

    create_save_to_clipboard(f"copy_btn_2", data[1]["name"])

    if "product_overview_improved" not in st.session_state:
        st.session_state.product_overview_improved = ""

    left_column, middle_column, right_column = st.columns([1, 4, 1])

    with middle_column:
        if st.button(
            data[2]["button_label"], key="btn_generate_3", use_container_width=True
        ):
            st.session_state.product_overview_improved = llm_run(
                model=data[2]["model"],
                temperature=data[2]["temperature"],
                template=data[2]["prompt"],
                **{
                    k: st.session_state.get(k, "")
                    for k in data[2]["input_params"].split(",")
                },
            )

    st.session_state.product_overview_improved = st.text_area(
        "product_overview_improved",
        label_visibility="collapsed",
        key="text_area_3",
        height=500,
        value=st.session_state.get("product_overview_improved", ""),
    )

    create_save_to_clipboard(f"copy_btn_3", data[2]["name"])

    if "technology_list" not in st.session_state:
        st.session_state.technology_list = ""

    left_column, right_column = st.columns([5, 1])
    with left_column:
        st.write(data[3]["button_label"])
    with right_column:
        if st.button("Regenerate", key="btn_generate_4", use_container_width=True):
            st.session_state.technology_list = llm_run(
                model=data[3]["model"],
                temperature=data[3]["temperature"],
                template=data[3]["prompt"],
                **{
                    k: st.session_state.get(k, "")
                    for k in data[3]["input_params"].split(",")
                },
            )

    st.session_state.technology_list = st.text_area(
        "technology_list",
        label_visibility="collapsed",
        key="text_area_4",
        value=st.session_state.get("technology_list", ""),
    )

    create_save_to_clipboard(f"copy_btn_4", data[3]["name"])

    if "innovation_list" not in st.session_state:
        st.session_state.innovation_list = ""

    st.write(data[4]["button_label"])
    left_column, right_column = st.columns([5, 1])
    with right_column:
        if st.button("Generate", key="btn_generate_5", use_container_width=True):
            st.session_state.innovation_list = llm_run(
                model=data[4]["model"],
                temperature=data[4]["temperature"],
                template=data[4]["prompt"],
                **{
                    k: st.session_state.get(k, "")
                    for k in data[4]["input_params"].split(",")
                },
            )

    st.session_state.innovation_list = st.text_area(
        "innovation_list",
        label_visibility="collapsed",
        key="text_area_5",
        value=st.session_state.get("innovation_list", ""),
    )

    create_save_to_clipboard(f"copy_btn_5", data[4]["name"])

    if "task_list" not in st.session_state:
        st.session_state.task_list = ""

    st.write(data[5]["button_label"])
    left_column, right_column = st.columns([5, 1])
    with right_column:
        if st.button("Generate", key="btn_generate_6", use_container_width=True):
            st.session_state.task_list = llm_run(
                model=data[5]["model"],
                temperature=data[5]["temperature"],
                template=data[5]["prompt"],
                **{
                    k: st.session_state.get(k, "")
                    for k in data[5]["input_params"].split(",")
                },
            )

    st.session_state.task_list = st.text_area(
        "task_list",
        label_visibility="collapsed",
        key="text_area_6",
        value=st.session_state.get("task_list", ""),
    )

    create_save_to_clipboard(f"copy_btn_6", data[5]["name"])


if __name__ == "__main__":
    main()
