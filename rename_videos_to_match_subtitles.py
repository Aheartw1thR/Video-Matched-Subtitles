import os

def rename_videos_to_match_subtitles(video_ext, srt_ext, directory):
    video_files = []
    srt_files = []

    for file in sorted(os.listdir(directory)):
        if file.endswith(video_ext):
            video_files.append(file)
        elif file.endswith(srt_ext):
            srt_files.append(file)

    if len(video_files) != len(srt_files):
        print("Error: The number of video files does not match the number of SRT files.")
        return

    for video, srt in zip(video_files, srt_files):
        video_name, _ = os.path.splitext(video)
        srt_name, _ = os.path.splitext(srt)

        if video_name != srt_name:
            new_video_name = f"{srt_name}{video_ext}"
            old_video_path = os.path.join(directory, video)
            new_video_path = os.path.join(directory, new_video_name)
            os.rename(old_video_path, new_video_path)
            print(f"Renamed '{video}' to '{new_video_name}'")

if __name__ == "__main__":
    # Set the directory path containing the video and SRT files
    directory = "I:/蜘蛛侠1994/蜘蛛侠1994 S5"
    
    # Set the extensions for video and SRT files (e.g., .mp4, .mkv, .avi, .srt)
    video_ext = ".mp4"
    srt_ext = ".srt"

    rename_videos_to_match_subtitles(video_ext, srt_ext, directory)
