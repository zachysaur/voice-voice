import gradio as gr
from TTS.api import TTS
import os

# Initialize the TTS model
api = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24")

# Ensure the 'results' directory exists
os.makedirs("results", exist_ok=True)

def greet(source, target):
    # Generate the file path in the 'results' folder
    output_file = os.path.join("results", "output.wav")

    print("Processing audio:", source, target, output_file)

    # Perform voice conversion and save to the 'results' folder
    api.voice_conversion_to_file(source_wav=source, target_wav=target, file_path=output_file)
    print("> Done")

    # Return the path to the output file
    return output_file

# Gradio interface setup
app = gr.Interface(
    fn=greet,
    inputs=[gr.Audio(type="filepath"), gr.Audio(type="filepath")],
    outputs=gr.Audio(type="filepath"),
)
app.queue(max_size=5000, concurrency_count=5)
app.launch(share=True)
