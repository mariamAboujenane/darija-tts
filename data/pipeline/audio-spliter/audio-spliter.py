"""module  for audio-spliter.py that splits audio files in a folder.

splited audio files are saved into smaller segments based on silence.
"""
import os
from pathlib import Path
from venv import logger

from pydub import AudioSegment
from pydub.silence import split_on_silence


class AudioSplitter:
    """Class for splitting audio files in a folder based on silence."""
    def __init__(self, input_folder : str ="cleaned_audios",  # noqa: PLR0913
                 output_folder : str ="wav",
                 silence_thresh : int =-40,
                 min_silence_len : int =500,
                 min_segment_length : int =10000,
                 max_segment_length : int =15000) -> None:
        """Initializes an instance of the AudioSplitter class.

        Args:
                input_folder (str, optional): The input folder containing
                the audio files to split. Defaults to "cleaned_audios".
                output_folder (str, optional): The output folder where the split audio
                files will be saved. Defaults to "wav".
                silence_thresh (int, optional): The threshold in decibels to
                determine silence. Defaults to -40.
                min_silence_len (int, optional): The minimum length in
                milliseconds of silence to consider as a split point. Defaults to 500.
                min_segment_length (int, optional): The minimum length in milliseconds
                of each split segment. Defaults to 10000.
                max_segment_length (int, optional): The maximum length in milliseconds
                of each split segment. Defaults to 15000.

        Returns:
                None
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.silence_thresh = silence_thresh
        self.min_silence_len = min_silence_len
        self.min_segment_length = min_segment_length
        self.max_segment_length = max_segment_length

        # Ensure output folder exists
        Path.mkdir(self.output_folder, parents=True)

    def process(self) -> None:
        """Processes the audio files in the input folder by splitting them into smaller segments.

        Iterates over all .wav files in the input folder, and for each file, it calls
        the split_audio method to split the file into smaller segments.

        Args:
            None

        Returns:
            None

        Raises:
            FileNotFoundError: If no .wav files are found in the input folder.
            Exception: If any other error occurs during the processing.
        """  # noqa: E501
        # Get all .wav files in the input folder
        try:
            audio_files = [f for f in os.listdir(self.input_folder) if
                           f.endswith(".wav")]
            if not audio_files:
                msg = f"No .wav files found in folder: {self.input_folder}"
                raise FileNotFoundError(msg)  # noqa: TRY301

            for audio_file in audio_files:
                self.split_audio(Path(self.input_folder) / audio_file)

        except Exception as e:  # noqa: BLE001
            logger.exception(f"An error occurred: {e}")

    def split_audio(self, file_path : str) -> None:
        """Splits an audio file into smaller segments based on silence.

        Args:
            file_path (str): The path to the audio file to be split.

        Returns:
            None

        Raises:
            Exception: If any error occurs during the processing of the audio file.
        """
        try:
            audio = AudioSegment.from_file(file_path)
            file_name = os.path.splitext(os.path.basename(file_path))[0]  # noqa: PTH119, PTH122
            output_dir = Path(self.output_folder) / file_name
            Path.mkdir(output_dir, parents=True)

            segments = split_on_silence(
                audio,
                min_silence_len=self.min_silence_len,
                silence_thresh=self.silence_thresh,
                keep_silence=200,
            )

            current_segment = AudioSegment.silent(duration=0)
            segment_start = 0

            for segment in segments:
                if len(current_segment) + len(segment) < self.min_segment_length:
                    current_segment += segment
                elif len(current_segment) + len(segment) > self.max_segment_length:
                    segment_end = segment_start + len(current_segment) // 1000
                    self.save_segment(current_segment,
                                      file_name,
                                      segment_start,
                                      segment_end)
                    segment_start = segment_end
                    current_segment = segment
                else:
                    current_segment += segment
                    segment_end = segment_start + len(current_segment) // 1000
                    self.save_segment(current_segment,
                                      file_name,
                                      segment_start,
                                      segment_end)
                    segment_start = segment_end
                    current_segment = AudioSegment.silent(duration=0)

            if len(current_segment) > 0:
                segment_end = segment_start + len(current_segment) // 1000
                self.save_segment(current_segment,
                                  file_name,
                                  segment_start,
                                  segment_end)

        except Exception as e:  # noqa: BLE001
            logger.exception(f"Failed to process {file_path}: {e}")

    def save_segment(self, segment: any, file_name: str,
                     start_time: int, end_time: int) -> None:
        """Saves a given audio segment to a file.

        Args:
            segment (AudioSegment): The audio segment to be saved.
            file_name (str): The base name of the file to be saved.
            start_time (int): The start time of the segment in seconds.
            end_time (int): The end time of the segment in seconds.

        Returns:
            None
        """
        try:
            segment_filename = f"{file_name}.{start_time}.{end_time}.wav"
            segment_path = Path(self.output_folder) / file_name / segment_filename
            segment.export(segment_path, format="wav")
            logger.info(f"Saved: {segment_path}")

        except Exception as e:  # noqa: BLE001
            logger.exception(f"Failed to save segment {file_name}: {e}")

# Usage example
splitter = AudioSplitter()
splitter.process()
