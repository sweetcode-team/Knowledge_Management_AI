import Link from 'next/link'
import { headers } from 'next/headers'
import { Button } from '@/components/ui/button'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { AlertTriangleIcon } from 'lucide-react'

export default function NotFound() {
    const headersList = headers()
    const domain = headersList.get('host')

    return (
        <div className='p-4 space-y-4'>
            <h2>Not Found</h2>
            <Alert variant="destructive" className='max-w-2xl'>
                <AlertTitle className='flex gap-2 items-center font-bold'>
                    <AlertTriangleIcon className='h-5 w-5' />
                    404 - Not Found
                </AlertTitle>
                <AlertDescription>Could not find requested resource.</AlertDescription>
            </Alert>
            <Button>
                <Link href={`http://${domain}`}>
                    Go back
                </Link>
            </Button>
        </div>
    )
}