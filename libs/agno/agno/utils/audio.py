import base64

from agno.utils.log import log_info


def write_audio_to_file(audio, filename: str):
    """
    Write base64 encoded audio file to disk.

    :param audio: Base64 encoded audio file
    :param filename: The filename to save the audio to
    """
    wav_bytes = base64.b64decode(audio)
    with open(filename, "wb") as f:
        f.write(wav_bytes)
    log_info(f"Audio file saved to {filename}")
