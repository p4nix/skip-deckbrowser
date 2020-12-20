from aqt import mw, gui_hooks

def choose_deck():
    config = mw.addonManager.getConfig(__name__)

    did = mw.col.decks.id_for_name(config["deckname"])
    if did is None:
        return

    mw.col.decks.select(did)

    mw.col.startTimebox()
    mw.moveToState("review")

gui_hooks.main_window_did_init.append(choose_deck)
