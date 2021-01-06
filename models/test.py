def test_insert():
    from mongo import Mongo
    form = {'type': 'test_insert', 'deleted': True, 'foo': 'haha'}
    Mongo.insert(form, deleted=False)
    x = Mongo._find()
    for i in x:
        print(i)


def test_update():
    from mongo import Mongo
    form = {'message': 'test_update', 'deleted': True, 'foo': 'haha'}
    a = Mongo.insert(form, deleted=False)
    form = {'message': 'test_updated'}
    a.update(form)
    x = Mongo._find()
    for i in x:
        print(i)


def test_find_one():
    from mongo import Mongo
    a = Mongo.find_one(type='mongo')
    print(a)


def test_find_by():
    from mongo import Mongo
    a = Mongo.find_by(type="mongo")
    for i in a:
        print(i)


if __name__ == '__main__':
    test_update()
