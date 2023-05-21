import { createClient } from 'microcms-js-sdk'

export const client = createClient({
  serviceDomain: process.env.MICRO_CMS_SERVICE_DOMAIN + '',
  apiKey: process.env.MICRO_CMS_API_KEY + '',
})

export const POST_LIST_ENDPOINT = 'content'
