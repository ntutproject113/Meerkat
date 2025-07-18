import { defineStore } from 'pinia'

export const useTodoStore = defineStore('todo', {
  state: () => ({
    items: [
      { label: '背英文單字', checked: false, key: 'eng', id: 0 },
      { label: '學習HTML', checked: false, key: 'html', id: 1 },
      { label: '學習JAVA', checked: true, key: 'java', id: 2 },
      { label: '財務管理', checked: false, key: 'finance', id: 3 }
    ]
  }),
  actions: {
    toggleItem(key) {
      const item = this.items.find(i => i.key === key)
      if (item) item.checked = !item.checked
    },
    checkItem(key) {
      const item = this.items.find(i => i.key === key)
      if (item) item.checked = true
    },
    setItems(newItems) {
      this.items = newItems
    }
  },
  persist: true // 若你使用 pinia-plugin-persistedstate，開啟這可自動存 localStorage
})
