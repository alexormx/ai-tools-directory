import { Box, Heading, Text, Stack, Badge } from '@chakra-ui/react';
import Link from 'next/link';

export default function ToolCard({ tool }: { tool: any }) {
  return (
    <Box as={Link} href={`/tools/${tool.slug}`} borderWidth='1px' rounded='md' p={4} _hover={{ shadow: 'md', textDecoration: 'none' }}>
      <Stack spacing={2}>
        <Heading as='h3' size='md'>{tool.name || 'Tool Name'}</Heading>
        <Text fontSize='sm' noOfLines={3}>{tool.description || 'Descripción pendiente.'}</Text>
        <Stack direction='row' spacing={2} wrap='wrap'>
          {(tool.categories || []).slice(0,3).map((c: any) => <Badge key={c.slug}>{c.name}</Badge>)}
        </Stack>
      </Stack>
    </Box>
  );
}