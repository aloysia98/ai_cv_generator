from backend.services.cv_generator import generate_cv
import sys

def main():
    print("Paste job description.")
    print("When finished, press CTRL+Z then Enter.\n")

    job_description = sys.stdin.read()

    if not job_description.strip():
        print("No job description provided.")
        return

    output_file = generate_cv(job_description)

    print(f"\nCV generated successfully: {output_file}")


if __name__ == "__main__":
    main()
