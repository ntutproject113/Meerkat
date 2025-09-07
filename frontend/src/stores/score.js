import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useScoreStore = defineStore('score', () => {
  const R = ref(0)
  const A = ref(0)
  const E = ref(0)
  const S = ref(0)
  const I = ref(0)
  const C = ref(0)

  function addScore(key, value) {
    switch (key) {
      case 'R': R.value += value; break
      case 'A': A.value += value; break
      case 'E': E.value += value; break
      case 'S': S.value += value; break
      case 'I': I.value += value; break
      case 'C': C.value += value; break
    }
  }

  function reset() {
    R.value = A.value = E.value = S.value = I.value = C.value = 0
  }

  return { R, A, E, S, I, C, addScore, reset }
})
