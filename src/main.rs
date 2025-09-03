use iced::{
    Element, Length,
    alignment::Vertical,
    widget::{button, column, container, row, scrollable, text, text_input},
};

#[derive(Debug, Clone)]
enum Message {
    LoadPressed,
    SavePressed,
    ChannelNameChanged(usize, String),
    ChannelUrlChanged(usize, String),
}

#[derive(Clone)]
struct Channel {
    name: String,
    url: String,
}

struct EJIPTVEditor {
    channels: Vec<Channel>,
}

impl Default for EJIPTVEditor {
    fn default() -> Self {
        Self {
            channels: vec![Channel {
                name: "Example Channel".to_string(),
                url: "http://example.com/stream".to_string(),
            }],
        }
    }
}

impl EJIPTVEditor {
    fn title(&self) -> String {
        "EJ IPTV editor".to_string()
    }

    fn update(&mut self, message: Message) {
        match message {
            Message::LoadPressed => {
                // TODO: load M3U file
            }
            Message::SavePressed => {
                // TODO: save to M3U file
            }
            Message::ChannelNameChanged(index, new_name) => {
                if let Some(ch) = self.channels.get_mut(index) {
                    ch.name = new_name;
                }
            }
            Message::ChannelUrlChanged(index, new_url) => {
                if let Some(ch) = self.channels.get_mut(index) {
                    ch.url = new_url;
                }
            }
        }
    }

fn main() -> iced::Result {
    iced::application(EJIPTVEditor::title, EJIPTVEditor::update, EJIPTVEditor::view)
        .antialiasing(true)
        .run()
}
