import couchdb
from celery import task

@task
def sync_couch():
    db_list = ['appointments', 'company_departments', 'company_entrance', 'resisted_items', 'vehicle', 'visitors',
               'visitors_location']
    seq_list = {}
    server = couchdb.Server()

    if len(server) > 0:
        for db in db_list:
            try:
                instance = server[db]
                changes = instance.changes()
                last_seq = changes['last_seq']
                if db in seq_list:
                    if seq_list[db] < last_seq:
                        id = changes[last_seq][last_seq]['id']
            except KeyError:
                pass
print('this is it')
sync_couch()