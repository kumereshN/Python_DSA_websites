import pytest

from anagrams import group_anagrams

from typing import List, Set


@pytest.mark.parametrize(
    "words,expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["ate", "eat", "tea"], ["nat", "tan"]],
        ),
        (
            ["bat", "tab", "bad", "dab", "nat", "tan"],
            [["bad", "dab"], ["bat", "tab"], ["nat", "tan"]]
        )
    ],
)
def test_group_anagrams(words: List[str], expected: Set[Set[str]]) -> None:
    result = [sorted(group) for group in group_anagrams(words)]
    expected = [sorted(group) for group in expected]
    for group in expected:
        assert group in result
    for group in result:
        assert group in expected