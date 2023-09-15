#Feature: Add two numbers
#  Scenario Outline: Add two numbers from the command line
#    Given the input pairs are <input_pairs>
#    When I add the input pairs
#    Then the sum of the input pairs is <expected_sum>
#
#    Examples:
#      | input_pairs   | expected_sum |
#      | (3, 4)        | 7            |
#      | (5, 7)        | 12           |

Feature: Verify squared numbers

Scenario Outline: Verify square for <number>
    Then the <number> squared is <result>

Examples: Static
  | number | result |
  |   1    |    1   |
  |   2    |    4   |
  |   3    |    9   |
  |   4    |   16   |

  @dynamic
  Scenario Outline: Verify square for <number>
    Then the <number> squared is <result>

Examples: Dynamic
  | number | result |
  |   .    |    .   |