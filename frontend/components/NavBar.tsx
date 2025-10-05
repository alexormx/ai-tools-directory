"use client";
import { Box, Flex, HStack, Link as ChakraLink, IconButton, useDisclosure, Stack } from '@chakra-ui/react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { HamburgerIcon, CloseIcon } from '@chakra-ui/icons';

const links = [
  { href: '/', label: 'Inicio' },
  { href: '/tools', label: 'Herramientas' },
  { href: '/news', label: 'Noticias' }
];

function NavLinks() {
  const pathname = usePathname();
  return (
    <HStack as={'nav'} spacing={4} alignItems="center">
      {links.map(l => (
        <ChakraLink
          key={l.href}
            as={Link}
            href={l.href}
            px={3}
            py={2}
            rounded={'md'}
            fontWeight={pathname === l.href ? 'bold' : 'medium'}
            _hover={{ textDecoration: 'none', bg: 'gray.100' }}
            bg={pathname === l.href ? 'gray.100' : 'transparent'}
        >
          {l.label}
        </ChakraLink>
      ))}
    </HStack>
  );
}

export default function NavBar() {
  const { isOpen, onOpen, onClose } = useDisclosure();
  return (
    <Box borderBottomWidth="1px" mb={4} px={4}>
      <Flex h={14} alignItems={'center'} justifyContent={'space-between'} maxW="7xl" mx="auto">
        <Flex align="center" gap={6}>
          <IconButton
            size={'sm'}
            icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
            aria-label={'Toggle Navigation'}
            display={{ base: 'inline-flex', md: 'none' }}
            onClick={isOpen ? onClose : onOpen}
          />
          <ChakraLink as={Link} href="/" fontWeight="bold" fontSize="lg" _hover={{ textDecoration: 'none' }}>
            AI Tools
          </ChakraLink>
          <Flex display={{ base: 'none', md: 'flex' }}>
            <NavLinks />
          </Flex>
        </Flex>
      </Flex>
      {isOpen && (
        <Box pb={4} display={{ md: 'none' }}>
          <Stack as={'nav'} spacing={2}>
            <NavLinks />
          </Stack>
        </Box>
      )}
    </Box>
  );
}
