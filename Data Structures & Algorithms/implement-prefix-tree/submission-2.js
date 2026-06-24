class TrieNode {
    constructor(){
        this.children = new Map();
        this.endOfWord = false;
    }
}

class PrefixTree {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let cur = this.root;

        for (let w of word){
            if (!cur.children.has(w)) cur.children.set(w, new TrieNode());
            cur = cur.children.get(w);
        }
        cur.endOfWord = true;
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        let cur = this.root;

        for (let w of word){
            if (!cur.children.has(w)) return false;
            cur = cur.children.get(w);
        }
        return cur.endOfWord;
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        let cur = this.root;

        for (let w of prefix){
            if (!cur.children.has(w)) return false;
            cur = cur.children.get(w);
        }
        return true;
    }
}
