"""Unit tests for emotion_detector."""

from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    """Tests for the emotion_detector function."""

    def test_emotion_detector(self):

        # Assertion for "I am glad this happened"
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"], "joy")

        # Assertion for "I am really mad about this"
        result1 = emotion_detector("I am really mad about this")
        self.assertEqual(result1["dominant_emotion"], "anger")

        # Assertion for "I feel disgusted just hearing about this"
        result1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result1["dominant_emotion"], "disgust")

        # Assertion for "I am so sad about this"
        result1 = emotion_detector("I am so sad about this")
        self.assertEqual(result1["dominant_emotion"], "sadness")

        # Assertion for "I am really afraid that this will happen"
        result1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result1["dominant_emotion"], "fear")

unittest.main()