from storage import Storage

def test_add():
    pass

def test_remove():

    print("Trying to remove existing key once ...")
    try:
        data = {"one": 1, "two": 2}
        test = Storage(data)
        key = "two"
        test.remove(key)
    except KeyError as e:
        print(e)
        print("Remove function failed with data:", data, " and key:", key)
    else:
        assert key not in test.data, "The key \"{}\" was not removed from storage.".format(key)

    print("Trying to remove key that does not exist ...")
    try:
        got_key_error = False
        data = {"one" : 1, "two" : 2}
        test = Storage(data)
        key = "three"
        test.remove(key)
    except KeyError as e:
        got_key_error = True
        assert str(e) == "'Key \"%s\" does not exist'" % key

    assert got_key_error, "Key error is not raised when key does not exist."

    pass

def test_set():
    pass

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    #test_add()
    test_remove()
    #test_set()
    test_get()

if __name__ == "__main__":
    run_tests()