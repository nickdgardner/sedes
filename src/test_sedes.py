import unittest

import hexameter.scan
import sedes

class TestAssign(unittest.TestCase):
    def test_assign(self):
        for line, expected in (
            # Od. 1.1
            ("ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ", (
                ("ἄνδρα", "1", "–⏑"),
                ("μοι", "2.5", "⏑"),
                ("ἔννεπε", "3", "–⏑⏑"),
                ("μοῦσα", "5", "–⏑"),
                ("πολύτροπον", "6.5", "⏑–⏑⏑"),
                ("ὃς", "9", "–"),
                ("μάλα", "10", "⏑⏑"),
                ("πολλὰ", "11", "––"),
            )),
            # Od. 6.71
            ("ὣς εἰπὼν δμώεσσιν ἐκέκλετο, τοὶ δ’ ἐπίθοντο.", (
                ("ὣς", "1", "–"),
                ("εἰπὼν", "2", "––"),
                ("δμώεσσιν", "4", "––⏑"),
                ("ἐκέκλετο", "6.5", "⏑–⏑⏑"),
                ("τοὶ", "9", "–"),
                ("δ’", "10", ""),
                ("ἐπίθοντο", "10", "⏑⏑––"),
            )),
            # Od. 6.72
            ("οἱ μὲν ἄρ’ ἐκτὸς ἄμαξαν ἐύτροχον ἡμιονείην", (
                ("οἱ", "1", "–"),
                ("μὲν", "2", "⏑"),
                ("ἄρ’", "2.5", "⏑"),
                ("ἐκτὸς", "3", "–⏑"),
                ("ἄμαξαν", "4.5", "⏑–⏑"),
                ("ἐύτροχον", "6.5", "⏑–⏑⏑"),
                ("ἡμιονείην", "9", "–⏑⏑––"),
            )),
            # Od. 6.73
            ("ὥπλεον, ἡμιόνους θ’ ὕπαγον ζεῦξάν θ’ ὑπ’ ἀπήνῃ·", (
                ("ὥπλεον", "1", "–⏑⏑"),
                ("ἡμιόνους", "3", "–⏑⏑–"),
                ("θ’", "6", ""),
                ("ὕπαγον", "6", "⏑⏑–"),
                ("ζεῦξάν", "8", "––"),
                ("θ’", "10", ""),
                ("ὑπ’", "10", "⏑"),
                ("ἀπήνῃ", "10.5", "⏑––"),
            )),
            # Od. 6.74
            ("κούρη δ’ ἐκ θαλάμοιο φέρεν ἐσθῆτα φαεινήν.", (
                ("κούρη", "1", "––"),
                ("δ’", "3", ""),
                ("ἐκ", "3", "–"),
                ("θαλάμοιο", "4", "⏑⏑–⏑"),
                ("φέρεν", "6.5", "⏑–"),
                ("ἐσθῆτα", "8", "––⏑"),
                ("φαεινήν", "10.5", "⏑––"),
            )),
            # Od. 6.75
            ("καὶ τὴν μὲν κατέθηκεν ἐυξέστῳ ἐπ’ ἀπήνῃ,", (
                ("καὶ", "1", "–"),
                ("τὴν", "2", "–"),
                ("μὲν", "3", "–"),
                ("κατέθηκεν", "4", "⏑⏑–⏑"),
                ("ἐυξέστῳ", "6.5", "⏑–––"),
                ("ἐπ’", "10", "⏑"),
                ("ἀπήνῃ", "10.5", "⏑––"),
            )),
        ):
            scansion, = hexameter.scan.analyze_line_metrical(line)
            self.assertEqual(sedes.assign(scansion), expected, repr(line))
