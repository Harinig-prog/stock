from services.sentiment_service import EnhancedSentimentAnalyzer


def test_keywords_inside_other_words_are_not_counted():
    analyzer = EnhancedSentimentAnalyzer()
    text = "company rolls out a software update to support enterprise windows users"

    counts = analyzer._count_keyword_matches(text)

    # "up" (update/support), "rise" (enterprise) and "win" (windows) used to match
    assert counts["positive"] == 0
    assert counts["neutral"] == 1  # "update"


def test_against_does_not_count_as_a_gain():
    analyzer = EnhancedSentimentAnalyzer()

    assert analyzer._analyze_financial_context("rupee slips against the dollar again") == 0.0


def test_inflected_keywords_still_match():
    analyzer = EnhancedSentimentAnalyzer()
    counts = analyzer._count_keyword_matches("shares gained as profits beat estimates and margins rise")

    assert counts["positive"] == 4  # gained, profits, beat, rise
    assert counts["negative"] == 0
