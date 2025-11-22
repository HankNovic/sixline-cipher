/*
SixLine Cipher - JavaScript Encoder/Decoder
Spec: SLC-1.0
Author: HankNovic

Implements the SixLine Cipher as defined in:
docs/SLC-1.0-SPEC.md

Base symbols (base-6 digits):
  0 -> "i"
  1 -> "!"
  2 -> "l"
  3 -> "I"
  4 -> "|"
  5 -> "¦"

Each encoded unit is a Symbol Pair (2-character string).
*/

const SYMBOLS = ["i", "!", "l", "I", "|", "¦"];
const ENC_MAP = {};
const DEC_MAP = {};

function buildTables() {
    // ------ Letters A–Z ------
    for (let i = 0; i < 26; i++) {
        const a = Math.floor(i / 6);
        const b = i % 6;
        const pair = SYMBOLS[a] + SYMBOLS[b];
        const letter = String.fromCharCode(65 + i);
        ENC_MAP[letter] = pair;
    }

    // ------ Digits 0–9 ------
    for (let i = 0; i < 10; i++) {
        const a = Math.floor(i / 6);
        const b = i % 6;
        const pair = SYMBOLS[a] + SYMBOLS[b];
        ENC_MAP[String(i)] = pair;
    }

    // ------ Whitespace & Punctuation (v1.0 recommended) ------
    ENC_MAP[" "] = "|l";  // space
    ENC_MAP["."] = "|I";  // period
    ENC_MAP[","] = "||";  // comma
    ENC_MAP["?"] = "|¦";  // question
    ENC_MAP["!"] = "¦i";  // exclamation

    // ------ Build reverse map ------
    for (const key in ENC_MAP) {
        DEC_MAP[ENC_MAP[key]] = key;
    }
}

buildTables();

// =====================================
// Encoder
// =====================================
export function encode(text, sep = " ") {
    const out = [];
    const upper = text.toUpperCase();

    for (const ch of upper) {
        if (ENC_MAP[ch]) {
            out.push(ENC_MAP[ch]);
        } else {
            throw new Error("Unsupported character for SixLine encoding: " + JSON.stringify(ch));
        }
    }

    return out.join(sep);
}

// =====================================
// Helper: split cipher into pairs
// =====================================
function splitPairs(cipher) {
    const trimmed = cipher.trim();
    if (trimmed.length === 0) return [];

    // If whitespace appears, assume already split
    const parts = trimmed.split(/\s+/);
    if (parts.length > 1) {
        // validate all pairs
        for (const p of parts) {
            if (p.length !== 2) {
                throw new Error("Invalid token length (expected 2): " + JSON.stringify(p));
            }
        }
        return parts;
    }

    // Otherwise treat as continuous
    if (trimmed.length % 2 !== 0) {
        throw new Error("Cipher length must be even for continuous mode.");
    }

    const arr = [];
    for (let i = 0; i < trimmed.length; i += 2) {
        arr.push(trimmed.slice(i, i + 2));
    }
    return arr;
}

// =====================================
// Decoder
// =====================================
export function decode(cipher) {
    const pairs = splitPairs(cipher);
    const out = [];

    for (const p of pairs) {
        if (DEC_MAP[p]) {
            out.push(DEC_MAP[p]);
        } else {
            throw new Error("Invalid SixLine symbol pair: " + JSON.stringify(p));
        }
    }

    return out.join("");
}

// =====================================
// Example if run in Node directly
// =====================================
if (typeof process !== "undefined" &&
    process.argv[1] &&
    process.argv[1].endsWith("slc.js")) {

    const sample = "HELLO WORLD";
    const encoded = encode(sample);
    const decoded = decode(encoded);

    console.log("Plain :", sample);
    console.log("Encoded:", encoded);
    console.log("Decoded:", decoded);
}
