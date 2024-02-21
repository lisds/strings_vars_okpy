test = {
  'name': 'Question defining_x',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'x'
          >>> # Have you run the cell defining 'x' yet?
          >>> 'x' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'x'
          >>> # from its initial state (of 0)
          >>> x != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Change the value of 'x' to 3.
          >>> x == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
