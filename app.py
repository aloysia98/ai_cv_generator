import gradio as gr
from backend.services.cv_generator import generate_cv

def run(job_description):
    return generate_cv(job_description)

demo = gr.Interface(
    fn=run,
    inputs=gr.Textbox(lines=18, label="Paste Job Description"),
    outputs=gr.File(label="Download CV PDF"),
    title="AI CV Generator"
)

if __name__ == "__main__":
    demo.launch()
