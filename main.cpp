#include "IPTV Editor"

int main() {
    // Create an instance of the IPTVEditor class
    IPTVEditor editor;

    // Open a new channel
    editor.openChannel("example.com/channel.m3u8");

    // Play the channel
    editor.play();

    // Stop the channel
    editor.stop();

    // Close the editor
    editor.close();

    return 0;
}
