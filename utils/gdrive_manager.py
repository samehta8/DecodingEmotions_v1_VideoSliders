"""
Local video file manager.
Handles video file operations from local filesystem.
"""
import os


def get_all_video_filenames(folder_path):
    """
    Get list of all video filenames in a local folder.

    Args:
        folder_path: Path to local video folder

    Returns:
        List of video filenames (e.g., ['event_001.mp4', 'event_002.mp4'])
    """
    if not os.path.exists(folder_path):
        print(f"[WARNING] Video folder not found: {folder_path}")
        return []

    try:
        # List all .mp4 files in the directory
        video_files = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith('.mp4')
        ]
        print(f"[INFO] Found {len(video_files)} video files in {folder_path}")
        return sorted(video_files)
    except Exception as e:
        print(f"[ERROR] Failed to list videos in {folder_path}: {e}")
        return []


def get_video_path(filename, folder_path):
    """
    Get the full local path for a video file.

    Args:
        filename: Video filename (e.g., 'event_001.mp4')
        folder_path: Path to local video folder

    Returns:
        Full path to video file, or None if file not found
    """
    if not folder_path:
        print("[ERROR] No folder path provided")
        return None

    full_path = os.path.join(folder_path, filename)

    if not os.path.exists(full_path):
        print(f"[WARNING] Video file not found: {full_path}")
        return None

    return full_path
