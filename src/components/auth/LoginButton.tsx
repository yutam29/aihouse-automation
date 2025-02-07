import { useAuth0 } from '@auth0/auth0-react';
import { MdLogin } from 'react-icons/md';

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return (
    <div
      className="cursor-pointer flex flex-row justify-start items-center gap-2"
      onClick={() => loginWithRedirect()}
    >
      <MdLogin className="text-xl " />
      Login
    </div>
  );
};

export default LoginButton;
