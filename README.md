# Action Recorder

Demo showcasing action-based videos. It basically logs all of the running processes, current mouse position and all keystrokes to later play them all back sequentially.

See the [demo](demo.mp4)

## Usage

Use `pipenv` to install dependencies.

```bash
pipenv install
pipenv shell
```

-   `save_video.py`: record a 10 second video
-   `play_video.py`: play back video (hardcoded video values)

## Thoughts

Using an action-based recorder is a really bad idea. Granted, recording actions instead of video can reduce file sizes and introduce more potentials for interactivity. However, it requires the user's desktop to mirror the exact same conditions as the recorder's, from the current running apps to the positioning of icons to the screen dimensions. I believe an action-based recorder would be better in the context of controlled environments (ie: just within a web browser) because you would be able to register what elements were clicked independent of device type, as opposed to mouse position.
