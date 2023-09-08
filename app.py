import gradio as gr
from gradio_client import Client
# Create a Gradio interface
def lyrics_translator(input_text, source_language, target_language):
    try:
        client = Client("https://facebook-seamless-m4t.hf.space/")
        result = client.predict(
            "T2TT (Text to Text translation)",
            "text",
            None,
            None,
            input_text,
            source_language,
            target_language,
            api_name="/run"
        )
        return result
    except Exception as e:
        return f"Error: {str(e)}"

gr_interface = gr.Interface(
    fn=lyrics_translator,
    inputs=[
        gr.inputs.Textbox(label="Enter the lyrics you want to translate"),
        gr.inputs.Dropdown(
            choices=["Afrikaans", "Amharic", "Armenian", "Assamese", "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian", "Burmese", "Cantonese", "Catalan", "Cebuano", "Central Kurdish", "Croatian", "Czech", "Danish", "Dutch", "Egyptian Arabic", "English", "Estonian", "Finnish", "French", "Galician", "Ganda", "Georgian", "German", "Greek", "Gujarati", "Halh Mongolian", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Kyrgyz", "Lao", "Lithuanian", "Luo", "Macedonian", "Maithili", "Malayalam", "Maltese", "Mandarin Chinese", "Marathi", "Meitei", "Modern Standard Arabic", "Moroccan Arabic", "Nepali", "North Azerbaijani", "Northern Uzbek", "Norwegian Bokmål", "Norwegian Nynorsk", "Nyanja", "Odia", "Polish", "Portuguese", "Punjabi", "Romanian", "Russian", "Serbian", "Shona", "Sindhi", "Slovak", "Slovenian", "Somali", "Southern Pashto", "Spanish", "Standard Latvian", "Standard Malay", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Telugu", "Thai", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh", "West Central Oromo", "Western Persian", "Yoruba", "Zulu"],
            label="Select source language"),
        gr.inputs.Dropdown(
            choices=["Bengali", "Catalan", "Czech", "Danish", "Dutch", "English", "Estonian", "Finnish", "French", "German", "Hindi", "Indonesian", "Italian", "Japanese", "Korean", "Maltese", "Mandarin Chinese", "Modern Standard Arabic", "Northern Uzbek", "Polish", "Portuguese", "Romanian", "Russian", "Slovak", "Spanish", "Swahili", "Swedish", "Tagalog", "Telugu", "Thai", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh", "Western Persian"],
            label="Select target language"),
    ],
    outputs=gr.outputs.Textbox(label="Translation Result"),
    live=True
)
gr_interface.launch()