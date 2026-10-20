
from moviepy import VideoFileClip
from pathlib import Path

# Enter the path of your video file
input_file = Path(r"C:\Users\YourName\Videos\input.mp4")

# Save the muted video in the same folder
output_file = input_file.with_name(
    f"{input_file.stem}_muted{input_file.suffix}"
)

try:
    with VideoFileClip(str(input_file)) as video:
        muted_video = video.without_audio()
        muted_video.write_videofile(
            str(output_file),
            codec="libx264",
            audio=False
        )

    print(f"\nSuccess! Muted video saved at:\n{output_file}")

except Exception as e:
    print(f"Error: {e}")
