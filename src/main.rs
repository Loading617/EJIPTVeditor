use iced::widget::{Button, Column, Row, Text, text_input, Scrollable};
use iced::{Alignment, Command, Element, Sandbox, Settings};

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

struct IPTVEditor {
    channels: Vec<Channel>,
}

impl Sandbox for EJIPTVEditor {
    type Message = Message;

    fn new() -> Self {
        Self {
            channels: vec![
                Channel {
                    name: "Example Channel".to_string(),
                    url: "http://example.com/stream".to_string(),
                },
            ],
        }
    }

    fn title(&self) -> String {
        "EJ IPTV editor".to_string()
    }

    fn update(&mut self, message: Self::Message) {
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

    fn view(&self) -> Element<Self::Message> {
        let mut content = column![text("EJ IPTV Playlist Editor").size(28)].spacing(20);

        let channel_list = self.channels.iter().enumerate().fold(
            column![].spacing(10),
            |col, (i, ch)| {
                col.push(
                    row![
                        text_input("Name", &ch.name, move |v| {
                            Message::ChannelNameChanged(i, v)
                        })
                        .width(iced::Length::FillPortion(2)),
                        text_input("URL", &ch.url, move |v| {
                            Message::ChannelUrlChanged(i, v)
                        })
                        .width(iced::Length::FillPortion(3)),
                    ]
                    .spacing(10),
                )
            },
        );

        content = content.push(
            scrollable(channel_list)
                .height(iced::Length::FillPortion(1))
                .padding(10),
        );

        content = content.push(
            row![
                button("Load Playlist").on_press(Message::LoadPressed),
                button("Save Playlist").on_press(Message::SavePressed),
            ]
            .spacing(20)
            .align_items(Alignment::Center),
        );

        content.into()
    }
}

fn main() -> iced::Result {
    EJIPTVEditor::run(Settings::default())
}
