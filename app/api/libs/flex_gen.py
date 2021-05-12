from linebot.models import (
    BubbleContainer, BoxComponent, TextComponent,
    BubbleStyle, BlockStyle
)

def header_creator(text):
    return BoxComponent(
        layout="vertical",
        contents=[
            TextComponent(
                text=text,
                size="md",
                weight="bold"
            )
        ]
    )

def baseline_creator(title, description):
    first_elmt = TextComponent(
        text=title,
        size="xs",
        flex=1,
        weight="bold"
    )

    second_elmt = TextComponent(
        text=description,
        size="xs",
        flex=5,
        wrap=True,
        color="#666666"
    )

    return BoxComponent(
        layout="baseline",
        spacing="sm",
        contents=[
            first_elmt,
            second_elmt
        ]
    )

def body_creator(events):
    contents = []

    for event in events:
        baselines = []
        baselines.append(baseline_creator("Proker", event.proker.name))
        baselines.append(baseline_creator("Title", event.name))
        baselines.append(baseline_creator("Date", event.date.strftime("%d %b %Y")))
        # print(type(event.date))
        contents.append(BoxComponent(
            layout="vertical",
            margin="xxl",
            spacing="sm",
            contents=baselines
        ))

    return BoxComponent(
        layout="vertical",
        contents=contents
    )

def flex_msg_gen(header, body):
    return BubbleContainer(
        header=header,
        body=body,
        styles=BubbleStyle(
            header=BlockStyle(separator=True),
            body=BlockStyle(separator=True)
        )
    )