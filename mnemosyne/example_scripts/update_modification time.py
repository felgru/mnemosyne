import copy
from mnemosyne.script import Mnemosyne

from mnemosyne.libmnemosyne.utils import MnemosyneError

# 'data_dir = None' will use the default system location, edit as appropriate.
data_dir = "C:\dot_test"
mnemosyne = Mnemosyne(data_dir)

created = {}
modified = {}

for _card_id, _fact_id in mnemosyne.database().cards():
    card = mnemosyne.database().card(_card_id, is_id_internal=True)
    created[card.id] = card.creation_time
    modified[card.id] = card.modification_time
mnemosyne.finalise()

# write

data_dir = None
mnemosyne = Mnemosyne(data_dir)

for id in created:
    print(id)
    mnemosyne.database().con.execute("""update cards set creation_time=?, modification_time=?
        where id=?""", (created[id], modified[id], id))
    try:
        card = mnemosyne.database().card(id, is_id_internal=False)
        mnemosyne.log().edited_card(card)
    except MnemosyneError:
        pass
mnemosyne.finalise()

