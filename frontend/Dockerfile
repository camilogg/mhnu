# Install dependencies only when needed
FROM node:lts-alpine AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /frontend
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Rebuild the source code only when needed
FROM node:lts-alpine AS builder
WORKDIR /frontend
COPY . .
COPY --from=deps /frontend/node_modules ./node_modules
RUN yarn build && yarn install --production --ignore-scripts --prefer-offline

# Production image, copy all the files and run next
FROM node:lts-alpine AS runner
WORKDIR /frontend

ENV NODE_ENV production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# You only need to copy next.config.js if you are NOT using the default configuration
COPY --from=builder /frontend/next.config.js ./
COPY --from=builder /frontend/.env.local ./.env.local
COPY --from=builder /frontend/public ./public
COPY --from=builder --chown=nextjs:nodejs /frontend/.next ./.next
COPY --from=builder /frontend/node_modules ./node_modules
COPY --from=builder /frontend/package.json ./package.json

USER nextjs

EXPOSE 3000

ENV PORT 3000

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry.
# ENV NEXT_TELEMETRY_DISABLED 1

CMD ["node_modules/.bin/next", "start"]
