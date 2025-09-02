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

    fn view(&self) -> Element<Message> {
        let mut content = column![text("EJ IPTV Playlist Editor").size(28)].spacing(20);

        let channel_list =
            self.channels
                .iter()
                .enumerate()
                .fold(column![].spacing(10), |col, (i, ch)| {
                    col.push(
                        row![
                            text_input("Name", &ch.name)
                                .on_input(move |v| { Message::ChannelNameChanged(i, v) })
                                .width(iced::Length::FillPortion(2)),
                            text_input("URL", &ch.url)
                                .on_input(move |v| { Message::ChannelUrlChanged(i, v) })
                                .width(iced::Length::FillPortion(3)),
                        ]
                        .spacing(10),
                    )
                });

        content = content.push(
            container(
                scrollable(channel_list)
                    .height(Length::Fill)
                    .width(Length::Fill),
            )
            .height(iced::Length::FillPortion(1))
            .padding(10),
        );

        content = content.push(
            row![
                button("Load Playlist").on_press(Message::LoadPressed),
                button("Save Playlist").on_press(Message::SavePressed),
            ]
            .spacing(20)
            .align_y(Vertical::Center),
        );

        content.into()
    }
}

fn main() -> iced::Result {
    iced::application(EJIPTVEditor::title, EJIPTVEditor::update, EJIPTVEditor::view)
        .antialiasing(true)
        .run()
}
