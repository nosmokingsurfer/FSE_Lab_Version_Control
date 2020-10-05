from storage import Storage

def test_add():
    pass


def test_remove_existing_key():
    print("Trying to remove existing key ...")
    try:
        data = {"one": 1, "two": 2}
        st = Storage(data)
        key = "two"
        st.remove(key)
    except KeyError as e:
        print(e)
        print("Remove function failed with data:", data, " and key:", key)
    else:
        assert key not in st.data, "The key \"{}\" was not removed from storage.".format(key)
        print("Ok")

def test_remove_absent_key():

    print("Trying to remove key that does not exist ...")
    try:
        got_key_error = False
        data = {"one" : 1, "two" : 2}
        st = Storage(data)
        key = "three"
        st.remove(key)
    except KeyError as e:
        got_key_error = True
        assert str(e) == "'Key \"%s\" does not exist'" % key

    assert got_key_error, "Key error is not raised when key does not exist."
    print("Ok")


def test_remove():

    test_remove_existing_key()

    test_remove_absent_key()    

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
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()