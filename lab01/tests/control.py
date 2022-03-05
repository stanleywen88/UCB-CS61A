test = {
  'name': 'Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          23
          >>> xk(10, 6)
          23
          >>> xk(4, 6)
          6
          >>> xk(0, 0)
          25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothing")
          >>> how_big(7)
          'big'
          >>> how_big(12)
          260c9a22fd4f3d2d25e08b6a0cd9d10e
          # locked
          >>> how_big(1)
          fdb47b226224360303fcfb56870d356a
          # locked
          >>> how_big(-1)
          d8e1cdfd7c1e2f4f4230deca5308e7c7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          6d6f378f0affa7f84aa38e519e353617
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          b0754f6baafe74512d1be0bd5c8098ed
          8e8a6ea9b75e03aef4652f8a6bc37fba
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        },
        {
          'code': r"""
          >>> positive = 28
          >>> while positive: # If this loops forever, just type Infinite Loop
          ...    print("positive?")
          ...    positive -= 3
          db3915202fb52c6613af5ef28bfc5773
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        },
        {
          'code': r"""
          >>> positive = -9
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if positive:
          ...        print(negative)
          ...    positive += 3
          ...    negative += 3
          b3c9c48be5cbc9295c81c3e75d1538d8
          efbd765b468a29852de43786a3d7f2b9
          3c05905385c5bd4c0ab5fe2640db2eed
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
