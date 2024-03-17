/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'avatars.githubusercontent.com',
            },
            {
                protocol: 'https',
                hostname: 'images.unsplash.com',
            },
        ],
    },
    webpack: (config, options) => {
        config.module.rules.push({
            test: /\bcanvas\.(node)/,
            use: 'raw-loader',
        })
        return config
    },
}

export default nextConfig
