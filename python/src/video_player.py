"""A video player class."""
import random

from .video_library import VideoLibrary


def sort_by_title(video):
    return video.title


library = VideoLibrary()
library_videos = library.get_all_videos()
current_video = None


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = library_videos
        videos.sort(key=sort_by_title)
        for video in videos:
            print(f"\t{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global current_video
        video_to_be_played = library.get_video(video_id)

        # getting the current playing video if any
        for video in library_videos:
            if video.get_playing_state():
                current_video = video

        # checking if there is a current video playing and playing the specified one
        if current_video:
            print(f"Stopping video: {current_video.title}")
            current_video.set_playing_state(False)

            print(f"Playing video: {video_to_be_played.title}")
            current_video = video_to_be_played
            current_video.set_playing_state(True)

        else:
            current_video = video_to_be_played
            current_video.set_playing_state(True)
            print(f"Playing video: {video_to_be_played.title}")

        if video_to_be_played is None:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        global current_video

        # getting the current playing video if any
        for video in library.get_all_videos():
            if video.get_playing_state():
                current_video = video
        if current_video:
            current_video.set_playing_state(False)
            print(f"Stopping video: {current_video.title}")
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        global current_video
        random_video = random.choice(library_videos)

        if not library_videos:
            print(" No videos available")
        elif current_video:
            print(f"Stopping video: {current_video.title}")
            current_video.set_playing_state(False)
            print(f"Playing video: {random_video.title}")
        else:
            current_video = random_video
            current_video.set_playing_state(True)
            print(f"Playing video: {random_video.title}")


    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
