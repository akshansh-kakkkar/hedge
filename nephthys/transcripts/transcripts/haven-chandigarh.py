from nephthys.transcripts.transcript import Transcript


class HavenChandigarh(Transcript):
    """Transcript for Hack Club Haven Chandigarh, powered by Hedgedog."""

    program_name: str = "Haven Chandigarh"
    program_owner: str = "YOUR_SLACK_USER_ID"

    help_channel: str = "C0C16L2HBL2"  # #haven-help
    ticket_channel: str = "C0C16L2HBL2"  # #haven-help
    team_channel: str = "C0C0RFM1VTR"  # #haven-staff

    first_ticket_create: str = f"""
🦔 Hey there (user)! Welcome to the Haven Chandigarh support channel!

I'm Hedgedog, and someone from the Haven team will be here to help you out soon.

Once your question has been answered, please hit the button below to mark this ticket as resolved!
"""

    ticket_create: str = f"""
🦔 Hey there (user)! Welcome back to the Haven Chandigarh support channel!

I'm Hedgedog, and someone from the Haven team should be along to help you soon.
"""

    resolve_ticket_button: str = "Mark As Resolved"

    ticket_resolve: str = f"""
🦔 <@{{user_id}}> has marked this ticket as resolved!

If you think this was a mistake, you can reopen the ticket.

Have another question? Feel free to send another message in <#{help_channel}> and we'll be happy to help!
"""

    not_allowed_channel: str = f"""
🦔 Hey! It looks like you're not supposed to be in this channel.

Please talk to <@{program_owner}> if you think this is a mistake.
"""

    faq_macro: str = ""
