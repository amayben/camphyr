

import datetime


def get_user_email():
    return auth.user.email if auth.user is not None else None

db.define_table('story',
                Field('user_email', default=get_user_email()),
                Field('title'),
                Field('snippets', 'text'),
                Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
                Field('is_public', 'boolean', default=True)
                )

db.story.user_email.writeable = False
db.story.user_email.readable = False
db.story.updated_on.writable = db.story.updated_on.readable = False



#optimize this later