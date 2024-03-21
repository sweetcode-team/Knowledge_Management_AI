import { NextRequest, NextResponse } from 'next/server'

async function getConfiguration() {
  //1000ms delay to simulate a real API call
  await new Promise((resolve) => setTimeout(resolve, 500))
  return true
}

export async function middleware(req: NextRequest) {
    const pathname = req.nextUrl.pathname

    if (req.nextUrl.pathname.startsWith("/_next")) {
      return NextResponse.next();
    }
  
    const isConfigurationSet = await getConfiguration()
    const isConfigurationPage = pathname.startsWith('/configuration')

    if (isConfigurationPage) {
      if (isConfigurationSet) {
        return NextResponse.redirect(new URL('/', req.url))
      }
      return NextResponse.next()
  }

    if (!isConfigurationSet) {
        return NextResponse.redirect(new URL('/configuration', req.url))
    }
    return NextResponse.next()
}

export const config = {
  matchter: ['/', '/chatbot', '/chatbot/:path*', '/documents', '/documents/:path*', '/settings', '/settings/:path*', '/configuration'],
}