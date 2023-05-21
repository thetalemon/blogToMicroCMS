export type Post = {
  id: string
  publishedAt: string
  revisedAt: string
  title: string
  content: string
  importData: {
    publishDate: string
    content: string
  }
  category: {
    id: string
    name: string
  }[]
}
