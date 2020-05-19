# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""" Command: .dab , .brain 

credit: lejend @r4v4n4"""

import random

from telethon import events, types, functions, utils


def choser(cmd, pack, blacklist={}):
    docs = None
    @borg.on(events.NewMessage(pattern=rf'\.{cmd}', outgoing=True))
    async def handler(event):
        await event.delete()

        nonlocal docs
        if docs is None:
            docs = [
                utils.get_input_document(x)
                for x in (await borg(functions.messages.GetStickerSetRequest(types.InputStickerSetShortName(pack)))).documents
                if x.id not in blacklist
            ]

        await event.respond(file=random.choice(docs))


choser('rstic', 'Shfik')
choser('rastic', 'Shfik')
choser('ranastic', 'Shfik')
choser('ranstic', 'Shfik', {
    
})
