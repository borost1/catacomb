world = [1, 2, 3, 4]
titles = []
description = []
obstacles = []
doors = []

skeleton_screen = {

    #create id, create description (add skeleton text, append words according to other items, description create end
    # of the code
    # , create choices 1-4, later in the game MAYBE 1-6 (cube), add obstacle from obstacle list
    # acle dictionary, dictionary_name[key] = value instead of append
    #according to the number of doors
{
        'id': (),
        'title': (),
        'description': (),
        'choices': [
            {
                'name': (),
                'text': (),
                'first_screen': (),
                "commands": print("You have  4 doors to choose from! These doors are labeled with 4 letters for some reason, a, b, c, d.")
            },
            {
                'name': (),
                'text': (),
                'second_screen': (),
            },
{
                'name': (),
                'text': (),
                'third_screen': (),
            },
{
                'name': (),
                'text': (),
                'fourth_screen': (),
            },
        ]
    },


}
OG_screens = [
    {
        'id': 0,
        'title': "Intro Screen",
        'description': "This is the first room",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
                "commands": print("You have  4 doors to choose from! These doors are labeled with 4 letters for some reason, a, b, c, d.")
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    },
 {
        'id': 1,
        'title': "spike_room",
        'description': "endless hole with spikes",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,

            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    }, {
        'id': 2,
        'title': "sphinx_room",
        'description': "riddles, questions to go further",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    }, {
        'id': 3,
        'title': "nice_room",
        'description': "just a nice room, nothing to see here",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    },
{
        'id': 4,
        'title': "secret_room",
        'description': "secret room, needs a key",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
{
        'id': 5,
        'title': "spike_roomNOT",
        'description': "endless hole with spikes",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,

            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    }, {
        'id': 6,
        'title': "sphinx_roomNOT",
        'description': "riddles, questions to go further",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    }, {
        'id': 7,
        'title': "nice_roomNOT",
        'description': "just a nice room, nothing to see here",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]
    },
{
        'id': 8,
        'title': "secret_roomNOT",
        'description': "secret room, needs a key",
        'choices': [
            {
                'name': "A",
                'text': "spike_room",
                'screen': 1,
            },
            {
                'name': "B",
                'text': "sphinx_room",
                'screen': 2,
            },
{
                'name': "C",
                'text': "nice_room",
                'screen': 3,
            },
{
                'name': "D",
                'text': "secret_room",
                'screen': 4,
            },
        ]


