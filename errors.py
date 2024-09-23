# command to run tests python -m pytest tests/
/home/nduta/burrenv_/lib/python3.10/site-packages/pytest_asyncio/plugin.py:208: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/nduta/burr_/tests
configfile: pytest.ini
plugins: anyio-4.4.0, asyncio-0.24.0
asyncio: mode=auto, default_loop_scope=None
collected 286 items / 3 skipped                                                

tests/core/test_action.py .............................................. [ 16%]
                                                                         [ 16%]
tests/core/test_application.py ......................................... [ 30%]
..............................................................           [ 52%]
tests/core/test_graph.py .......                                         [ 54%]
tests/core/test_graphviz_display.py FFFF.                                                                                                                                                           [ 56%]
tests/core/test_implementations.py .                                                                                                                                                                [ 56%]
tests/core/test_persistence.py .......                                                                                                                                                              [ 59%]
tests/core/test_serde.py ........                                                                                                                                                                   [ 61%]
tests/core/test_state.py .........................                                                                                                                                                  [ 70%]
tests/core/test_validation.py ..                                                                                                                                                                    [ 71%]
tests/integration_tests/test_app.py ..                                                                                                                                                              [ 72%]
tests/integrations/serde/test_langchain.py ...                                                                                                                                                      [ 73%]
tests/integrations/serde/test_pandas.py .                                                                                                                                                           [ 73%]
tests/integrations/serde/test_pickle.py .                                                                                                                                                           [ 73%]
tests/integrations/serde/test_pydantic.py .                                                                                                                                                         [ 74%]
tests/integrations/test_burr_hamilton.py .......                                                                                                                                                    [ 76%]
tests/integrations/test_burr_opentelemetry.py .......                                                                                                                                               [ 79%]
tests/integrations/test_burr_pydantic.py ..............................                                                                                                                             [ 89%]
tests/integrations/test_opentelemetry.py .                                                                                                                                                          [ 89%]
tests/test_end_to_end.py .F                                                                                                                                                                         [ 90%]
tests/tracking/test_common_models.py .                                                                                                                                                              [ 90%]
tests/tracking/test_local_tracking_client.py ..............                                                                                                                                         [ 95%]
tests/visibility/test_tracing.py ............                                                                                                                                                       [100%]

================================================================================================ FAILURES =================================================================================================
__________________________________________________________________________________ test_visualize_dot_output[app-False] ___________________________________________________________________________________

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f79785af0>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
>               proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:96: in _run_input_lines
    popen = subprocess.Popen(cmd, stdin=subprocess.PIPE, **kwargs)
/usr/lib/python3.10/subprocess.py:971: in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Popen: returncode: 255 args: [PosixPath('dot'), '-Kdot', '-Tpng']>, args = [PosixPath('dot'), '-Kdot', '-Tpng'], executable = b'dot', preexec_fn = None, close_fds = True, pass_fds = ()
cwd = None, env = None, startupinfo = None, creationflags = 0, shell = False, p2cread = 14, p2cwrite = 15, c2pread = 16, c2pwrite = 17, errread = 18, errwrite = 19, restore_signals = True, gid = None
gids = None, uid = None, umask = -1, start_new_session = False

    def _execute_child(self, args, executable, preexec_fn, close_fds,
                       pass_fds, cwd, env,
                       startupinfo, creationflags, shell,
                       p2cread, p2cwrite,
                       c2pread, c2pwrite,
                       errread, errwrite,
                       restore_signals,
                       gid, gids, uid, umask,
                       start_new_session):
        """Execute program (POSIX version)"""
    
        if isinstance(args, (str, bytes)):
            args = [args]
        elif isinstance(args, os.PathLike):
            if shell:
                raise TypeError('path-like args is not allowed when '
                                'shell is true')
            args = [args]
        else:
            args = list(args)
    
        if shell:
            # On Android the default shell is at '/system/bin/sh'.
            unix_shell = ('/system/bin/sh' if
                      hasattr(sys, 'getandroidapilevel') else '/bin/sh')
            args = [unix_shell, "-c"] + args
            if executable:
                args[0] = executable
    
        if executable is None:
            executable = args[0]
    
        sys.audit("subprocess.Popen", executable, args, cwd, env)
    
        if (_USE_POSIX_SPAWN
                and os.path.dirname(executable)
                and preexec_fn is None
                and not close_fds
                and not pass_fds
                and cwd is None
                and (p2cread == -1 or p2cread > 2)
                and (c2pwrite == -1 or c2pwrite > 2)
                and (errwrite == -1 or errwrite > 2)
                and not start_new_session
                and gid is None
                and gids is None
                and uid is None
                and umask < 0):
            self._posix_spawn(args, executable, env, restore_signals,
                              p2cread, p2cwrite,
                              c2pread, c2pwrite,
                              errread, errwrite)
            return
    
        orig_executable = executable
    
        # For transferring possible exec failure from child to parent.
        # Data format: "exception name:hex errno:description"
        # Pickle is not used; it is complex and involves memory allocation.
        errpipe_read, errpipe_write = os.pipe()
        # errpipe_write must not be in the standard io 0, 1, or 2 fd range.
        low_fds_to_close = []
        while errpipe_write < 3:
            low_fds_to_close.append(errpipe_write)
            errpipe_write = os.dup(errpipe_write)
        for low_fd in low_fds_to_close:
            os.close(low_fd)
        try:
            try:
                # We must avoid complex work that could involve
                # malloc or free in the child process to avoid
                # potential deadlocks, thus we do all this here.
                # and pass it to fork_exec()
    
                if env is not None:
                    env_list = []
                    for k, v in env.items():
                        k = os.fsencode(k)
                        if b'=' in k:
                            raise ValueError("illegal environment variable name")
                        env_list.append(k + b'=' + os.fsencode(v))
                else:
                    env_list = None  # Use execv instead of execve.
                executable = os.fsencode(executable)
                if os.path.dirname(executable):
                    executable_list = (executable,)
                else:
                    # This matches the behavior of os._execvpe().
                    executable_list = tuple(
                        os.path.join(os.fsencode(dir), executable)
                        for dir in os.get_exec_path(env))
                fds_to_keep = set(pass_fds)
                fds_to_keep.add(errpipe_write)
                self.pid = _posixsubprocess.fork_exec(
                        args, executable_list,
                        close_fds, tuple(sorted(map(int, fds_to_keep))),
                        cwd, env_list,
                        p2cread, p2cwrite, c2pread, c2pwrite,
                        errread, errwrite,
                        errpipe_read, errpipe_write,
                        restore_signals, start_new_session,
                        gid, gids, uid, umask,
                        preexec_fn)
                self._child_created = True
            finally:
                # be sure the FD is closed no matter what
                os.close(errpipe_write)
    
            self._close_pipe_fds(p2cread, p2cwrite,
                                 c2pread, c2pwrite,
                                 errread, errwrite)
    
            # Wait for exec to fail or succeed; possibly raising an
            # exception (limited in size)
            errpipe_data = bytearray()
            while True:
                part = os.read(errpipe_read, 50000)
                errpipe_data += part
                if not part or len(errpipe_data) > 50000:
                    break
        finally:
            # be sure the FD is closed no matter what
            os.close(errpipe_read)
    
        if errpipe_data:
            try:
                pid, sts = os.waitpid(self.pid, 0)
                if pid == self.pid:
                    self._handle_exitstatus(sts)
                else:
                    self.returncode = sys.maxsize
            except ChildProcessError:
                pass
    
            try:
                exception_name, hex_errno, err_msg = (
                        errpipe_data.split(b':', 2))
                # The encoding here should match the encoding
                # written in by the subprocess implementations
                # like _posixsubprocess
                err_msg = err_msg.decode()
            except ValueError:
                exception_name = b'SubprocessError'
                hex_errno = b'0'
                err_msg = 'Bad exception data from child: {!r}'.format(
                              bytes(errpipe_data))
            child_exception_type = getattr(
                    builtins, exception_name.decode('ascii'),
                    SubprocessError)
            if issubclass(child_exception_type, OSError) and hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = (err_msg == "noexec")
                if child_exec_never_called:
                    err_msg = ""
                    # The error must be from chdir(cwd).
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: PosixPath('dot')

/usr/lib/python3.10/subprocess.py:1863: FileNotFoundError

The above exception was the direct cause of the following exception:

graph = Graph(actions=[counter: count -> count], transitions=[Transition(from_=counter: count -> count, to=counter: count -> count, condition=condition: default)])
tmp_path = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_0'), filename = 'app', write_dot = False

    @pytest.mark.parametrize(
        "filename, write_dot", [("app", False), ("app.png", False), ("app", True), ("app.png", True)]
    )
    def test_visualize_dot_output(graph, tmp_path: pathlib.Path, filename: str, write_dot: bool):
        """Handle file generation with `graph.Digraph` `.render()` and `.pipe()`"""
        output_file_path = f"{tmp_path}/{filename}"
    
>       graph.visualize(
            output_file_path=output_file_path,
            write_dot=write_dot,
        )

tests/core/test_graphviz_display.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/graph.py:211: in visualize
    _render_graphviz(
burr/core/graph.py:86: in _render_graphviz
    graphviz_obj.pipe(format=format)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:104: in pipe
    return self._pipe_legacy(format,
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:121: in _pipe_legacy
    return self._pipe_future(format,
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:161: in _pipe_future
    return self._pipe_lines(*args, input_encoding=self.encoding, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/backend/piping.py:161: in pipe_lines
    proc = execute.run_check(cmd, capture_output=True, quiet=quiet, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f79785af0>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
                proc = subprocess.run(cmd, **kwargs)
        except OSError as e:
            if e.errno == errno.ENOENT:
>               raise ExecutableNotFound(cmd) from e
E               graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:81: ExecutableNotFound
________________________________________________________________________________ test_visualize_dot_output[app.png-False] _________________________________________________________________________________

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f7962a180>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
>               proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:96: in _run_input_lines
    popen = subprocess.Popen(cmd, stdin=subprocess.PIPE, **kwargs)
/usr/lib/python3.10/subprocess.py:971: in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Popen: returncode: 255 args: [PosixPath('dot'), '-Kdot', '-Tpng']>, args = [PosixPath('dot'), '-Kdot', '-Tpng'], executable = b'dot', preexec_fn = None, close_fds = True, pass_fds = ()
cwd = None, env = None, startupinfo = None, creationflags = 0, shell = False, p2cread = 14, p2cwrite = 15, c2pread = 16, c2pwrite = 17, errread = 18, errwrite = 19, restore_signals = True, gid = None
gids = None, uid = None, umask = -1, start_new_session = False

    def _execute_child(self, args, executable, preexec_fn, close_fds,
                       pass_fds, cwd, env,
                       startupinfo, creationflags, shell,
                       p2cread, p2cwrite,
                       c2pread, c2pwrite,
                       errread, errwrite,
                       restore_signals,
                       gid, gids, uid, umask,
                       start_new_session):
        """Execute program (POSIX version)"""
    
        if isinstance(args, (str, bytes)):
            args = [args]
        elif isinstance(args, os.PathLike):
            if shell:
                raise TypeError('path-like args is not allowed when '
                                'shell is true')
            args = [args]
        else:
            args = list(args)
    
        if shell:
            # On Android the default shell is at '/system/bin/sh'.
            unix_shell = ('/system/bin/sh' if
                      hasattr(sys, 'getandroidapilevel') else '/bin/sh')
            args = [unix_shell, "-c"] + args
            if executable:
                args[0] = executable
    
        if executable is None:
            executable = args[0]
    
        sys.audit("subprocess.Popen", executable, args, cwd, env)
    
        if (_USE_POSIX_SPAWN
                and os.path.dirname(executable)
                and preexec_fn is None
                and not close_fds
                and not pass_fds
                and cwd is None
                and (p2cread == -1 or p2cread > 2)
                and (c2pwrite == -1 or c2pwrite > 2)
                and (errwrite == -1 or errwrite > 2)
                and not start_new_session
                and gid is None
                and gids is None
                and uid is None
                and umask < 0):
            self._posix_spawn(args, executable, env, restore_signals,
                              p2cread, p2cwrite,
                              c2pread, c2pwrite,
                              errread, errwrite)
            return
    
        orig_executable = executable
    
        # For transferring possible exec failure from child to parent.
        # Data format: "exception name:hex errno:description"
        # Pickle is not used; it is complex and involves memory allocation.
        errpipe_read, errpipe_write = os.pipe()
        # errpipe_write must not be in the standard io 0, 1, or 2 fd range.
        low_fds_to_close = []
        while errpipe_write < 3:
            low_fds_to_close.append(errpipe_write)
            errpipe_write = os.dup(errpipe_write)
        for low_fd in low_fds_to_close:
            os.close(low_fd)
        try:
            try:
                # We must avoid complex work that could involve
                # malloc or free in the child process to avoid
                # potential deadlocks, thus we do all this here.
                # and pass it to fork_exec()
    
                if env is not None:
                    env_list = []
                    for k, v in env.items():
                        k = os.fsencode(k)
                        if b'=' in k:
                            raise ValueError("illegal environment variable name")
                        env_list.append(k + b'=' + os.fsencode(v))
                else:
                    env_list = None  # Use execv instead of execve.
                executable = os.fsencode(executable)
                if os.path.dirname(executable):
                    executable_list = (executable,)
                else:
                    # This matches the behavior of os._execvpe().
                    executable_list = tuple(
                        os.path.join(os.fsencode(dir), executable)
                        for dir in os.get_exec_path(env))
                fds_to_keep = set(pass_fds)
                fds_to_keep.add(errpipe_write)
                self.pid = _posixsubprocess.fork_exec(
                        args, executable_list,
                        close_fds, tuple(sorted(map(int, fds_to_keep))),
                        cwd, env_list,
                        p2cread, p2cwrite, c2pread, c2pwrite,
                        errread, errwrite,
                        errpipe_read, errpipe_write,
                        restore_signals, start_new_session,
                        gid, gids, uid, umask,
                        preexec_fn)
                self._child_created = True
            finally:
                # be sure the FD is closed no matter what
                os.close(errpipe_write)
    
            self._close_pipe_fds(p2cread, p2cwrite,
                                 c2pread, c2pwrite,
                                 errread, errwrite)
    
            # Wait for exec to fail or succeed; possibly raising an
            # exception (limited in size)
            errpipe_data = bytearray()
            while True:
                part = os.read(errpipe_read, 50000)
                errpipe_data += part
                if not part or len(errpipe_data) > 50000:
                    break
        finally:
            # be sure the FD is closed no matter what
            os.close(errpipe_read)
    
        if errpipe_data:
            try:
                pid, sts = os.waitpid(self.pid, 0)
                if pid == self.pid:
                    self._handle_exitstatus(sts)
                else:
                    self.returncode = sys.maxsize
            except ChildProcessError:
                pass
    
            try:
                exception_name, hex_errno, err_msg = (
                        errpipe_data.split(b':', 2))
                # The encoding here should match the encoding
                # written in by the subprocess implementations
                # like _posixsubprocess
                err_msg = err_msg.decode()
            except ValueError:
                exception_name = b'SubprocessError'
                hex_errno = b'0'
                err_msg = 'Bad exception data from child: {!r}'.format(
                              bytes(errpipe_data))
            child_exception_type = getattr(
                    builtins, exception_name.decode('ascii'),
                    SubprocessError)
            if issubclass(child_exception_type, OSError) and hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = (err_msg == "noexec")
                if child_exec_never_called:
                    err_msg = ""
                    # The error must be from chdir(cwd).
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: PosixPath('dot')

/usr/lib/python3.10/subprocess.py:1863: FileNotFoundError

The above exception was the direct cause of the following exception:

graph = Graph(actions=[counter: count -> count], transitions=[Transition(from_=counter: count -> count, to=counter: count -> count, condition=condition: default)])
tmp_path = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_1'), filename = 'app.png', write_dot = False

    @pytest.mark.parametrize(
        "filename, write_dot", [("app", False), ("app.png", False), ("app", True), ("app.png", True)]
    )
    def test_visualize_dot_output(graph, tmp_path: pathlib.Path, filename: str, write_dot: bool):
        """Handle file generation with `graph.Digraph` `.render()` and `.pipe()`"""
        output_file_path = f"{tmp_path}/{filename}"
    
>       graph.visualize(
            output_file_path=output_file_path,
            write_dot=write_dot,
        )

tests/core/test_graphviz_display.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/graph.py:211: in visualize
    _render_graphviz(
burr/core/graph.py:86: in _render_graphviz
    graphviz_obj.pipe(format=format)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:104: in pipe
    return self._pipe_legacy(format,
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:121: in _pipe_legacy
    return self._pipe_future(format,
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:161: in _pipe_future
    return self._pipe_lines(*args, input_encoding=self.encoding, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/backend/piping.py:161: in pipe_lines
    proc = execute.run_check(cmd, capture_output=True, quiet=quiet, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f7962a180>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
                proc = subprocess.run(cmd, **kwargs)
        except OSError as e:
            if e.errno == errno.ENOENT:
>               raise ExecutableNotFound(cmd) from e
E               graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:81: ExecutableNotFound
___________________________________________________________________________________ test_visualize_dot_output[app-True] ___________________________________________________________________________________

cmd = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], input_lines = None, encoding = None, quiet = False
kwargs = {'capture_output': True, 'cwd': PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_2'), 'startupinfo': None}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
>               proc = subprocess.run(cmd, **kwargs)

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:78: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/lib/python3.10/subprocess.py:503: in run
    with Popen(*popenargs, **kwargs) as process:
/usr/lib/python3.10/subprocess.py:971: in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Popen: returncode: 255 args: [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app']>, args = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], executable = b'dot', preexec_fn = None, close_fds = True
pass_fds = (), cwd = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_2'), env = None, startupinfo = None, creationflags = 0, shell = False, p2cread = -1, p2cwrite = -1
c2pread = 14, c2pwrite = 15, errread = 16, errwrite = 17, restore_signals = True, gid = None, gids = None, uid = None, umask = -1, start_new_session = False

    def _execute_child(self, args, executable, preexec_fn, close_fds,
                       pass_fds, cwd, env,
                       startupinfo, creationflags, shell,
                       p2cread, p2cwrite,
                       c2pread, c2pwrite,
                       errread, errwrite,
                       restore_signals,
                       gid, gids, uid, umask,
                       start_new_session):
        """Execute program (POSIX version)"""
    
        if isinstance(args, (str, bytes)):
            args = [args]
        elif isinstance(args, os.PathLike):
            if shell:
                raise TypeError('path-like args is not allowed when '
                                'shell is true')
            args = [args]
        else:
            args = list(args)
    
        if shell:
            # On Android the default shell is at '/system/bin/sh'.
            unix_shell = ('/system/bin/sh' if
                      hasattr(sys, 'getandroidapilevel') else '/bin/sh')
            args = [unix_shell, "-c"] + args
            if executable:
                args[0] = executable
    
        if executable is None:
            executable = args[0]
    
        sys.audit("subprocess.Popen", executable, args, cwd, env)
    
        if (_USE_POSIX_SPAWN
                and os.path.dirname(executable)
                and preexec_fn is None
                and not close_fds
                and not pass_fds
                and cwd is None
                and (p2cread == -1 or p2cread > 2)
                and (c2pwrite == -1 or c2pwrite > 2)
                and (errwrite == -1 or errwrite > 2)
                and not start_new_session
                and gid is None
                and gids is None
                and uid is None
                and umask < 0):
            self._posix_spawn(args, executable, env, restore_signals,
                              p2cread, p2cwrite,
                              c2pread, c2pwrite,
                              errread, errwrite)
            return
    
        orig_executable = executable
    
        # For transferring possible exec failure from child to parent.
        # Data format: "exception name:hex errno:description"
        # Pickle is not used; it is complex and involves memory allocation.
        errpipe_read, errpipe_write = os.pipe()
        # errpipe_write must not be in the standard io 0, 1, or 2 fd range.
        low_fds_to_close = []
        while errpipe_write < 3:
            low_fds_to_close.append(errpipe_write)
            errpipe_write = os.dup(errpipe_write)
        for low_fd in low_fds_to_close:
            os.close(low_fd)
        try:
            try:
                # We must avoid complex work that could involve
                # malloc or free in the child process to avoid
                # potential deadlocks, thus we do all this here.
                # and pass it to fork_exec()
    
                if env is not None:
                    env_list = []
                    for k, v in env.items():
                        k = os.fsencode(k)
                        if b'=' in k:
                            raise ValueError("illegal environment variable name")
                        env_list.append(k + b'=' + os.fsencode(v))
                else:
                    env_list = None  # Use execv instead of execve.
                executable = os.fsencode(executable)
                if os.path.dirname(executable):
                    executable_list = (executable,)
                else:
                    # This matches the behavior of os._execvpe().
                    executable_list = tuple(
                        os.path.join(os.fsencode(dir), executable)
                        for dir in os.get_exec_path(env))
                fds_to_keep = set(pass_fds)
                fds_to_keep.add(errpipe_write)
                self.pid = _posixsubprocess.fork_exec(
                        args, executable_list,
                        close_fds, tuple(sorted(map(int, fds_to_keep))),
                        cwd, env_list,
                        p2cread, p2cwrite, c2pread, c2pwrite,
                        errread, errwrite,
                        errpipe_read, errpipe_write,
                        restore_signals, start_new_session,
                        gid, gids, uid, umask,
                        preexec_fn)
                self._child_created = True
            finally:
                # be sure the FD is closed no matter what
                os.close(errpipe_write)
    
            self._close_pipe_fds(p2cread, p2cwrite,
                                 c2pread, c2pwrite,
                                 errread, errwrite)
    
            # Wait for exec to fail or succeed; possibly raising an
            # exception (limited in size)
            errpipe_data = bytearray()
            while True:
                part = os.read(errpipe_read, 50000)
                errpipe_data += part
                if not part or len(errpipe_data) > 50000:
                    break
        finally:
            # be sure the FD is closed no matter what
            os.close(errpipe_read)
    
        if errpipe_data:
            try:
                pid, sts = os.waitpid(self.pid, 0)
                if pid == self.pid:
                    self._handle_exitstatus(sts)
                else:
                    self.returncode = sys.maxsize
            except ChildProcessError:
                pass
    
            try:
                exception_name, hex_errno, err_msg = (
                        errpipe_data.split(b':', 2))
                # The encoding here should match the encoding
                # written in by the subprocess implementations
                # like _posixsubprocess
                err_msg = err_msg.decode()
            except ValueError:
                exception_name = b'SubprocessError'
                hex_errno = b'0'
                err_msg = 'Bad exception data from child: {!r}'.format(
                              bytes(errpipe_data))
            child_exception_type = getattr(
                    builtins, exception_name.decode('ascii'),
                    SubprocessError)
            if issubclass(child_exception_type, OSError) and hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = (err_msg == "noexec")
                if child_exec_never_called:
                    err_msg = ""
                    # The error must be from chdir(cwd).
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: PosixPath('dot')

/usr/lib/python3.10/subprocess.py:1863: FileNotFoundError

The above exception was the direct cause of the following exception:

graph = Graph(actions=[counter: count -> count], transitions=[Transition(from_=counter: count -> count, to=counter: count -> count, condition=condition: default)])
tmp_path = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_2'), filename = 'app', write_dot = True

    @pytest.mark.parametrize(
        "filename, write_dot", [("app", False), ("app.png", False), ("app", True), ("app.png", True)]
    )
    def test_visualize_dot_output(graph, tmp_path: pathlib.Path, filename: str, write_dot: bool):
        """Handle file generation with `graph.Digraph` `.render()` and `.pipe()`"""
        output_file_path = f"{tmp_path}/{filename}"
    
>       graph.visualize(
            output_file_path=output_file_path,
            write_dot=write_dot,
        )

tests/core/test_graphviz_display.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/graph.py:211: in visualize
    _render_graphviz(
burr/core/graph.py:82: in _render_graphviz
    graphviz_obj.render(path_without_suffix, format=format, view=view)
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/rendering.py:122: in render
    rendered = self._render(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/backend/rendering.py:326: in render
    execute.run_check(cmd,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cmd = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], input_lines = None, encoding = None, quiet = False
kwargs = {'capture_output': True, 'cwd': PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_2'), 'startupinfo': None}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
                proc = subprocess.run(cmd, **kwargs)
        except OSError as e:
            if e.errno == errno.ENOENT:
>               raise ExecutableNotFound(cmd) from e
E               graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:81: ExecutableNotFound
_________________________________________________________________________________ test_visualize_dot_output[app.png-True] _________________________________________________________________________________

cmd = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], input_lines = None, encoding = None, quiet = False
kwargs = {'capture_output': True, 'cwd': PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_3'), 'startupinfo': None}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
>               proc = subprocess.run(cmd, **kwargs)

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:78: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/usr/lib/python3.10/subprocess.py:503: in run
    with Popen(*popenargs, **kwargs) as process:
/usr/lib/python3.10/subprocess.py:971: in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Popen: returncode: 255 args: [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app']>, args = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], executable = b'dot', preexec_fn = None, close_fds = True
pass_fds = (), cwd = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_3'), env = None, startupinfo = None, creationflags = 0, shell = False, p2cread = -1, p2cwrite = -1
c2pread = 14, c2pwrite = 15, errread = 16, errwrite = 17, restore_signals = True, gid = None, gids = None, uid = None, umask = -1, start_new_session = False

    def _execute_child(self, args, executable, preexec_fn, close_fds,
                       pass_fds, cwd, env,
                       startupinfo, creationflags, shell,
                       p2cread, p2cwrite,
                       c2pread, c2pwrite,
                       errread, errwrite,
                       restore_signals,
                       gid, gids, uid, umask,
                       start_new_session):
        """Execute program (POSIX version)"""
    
        if isinstance(args, (str, bytes)):
            args = [args]
        elif isinstance(args, os.PathLike):
            if shell:
                raise TypeError('path-like args is not allowed when '
                                'shell is true')
            args = [args]
        else:
            args = list(args)
    
        if shell:
            # On Android the default shell is at '/system/bin/sh'.
            unix_shell = ('/system/bin/sh' if
                      hasattr(sys, 'getandroidapilevel') else '/bin/sh')
            args = [unix_shell, "-c"] + args
            if executable:
                args[0] = executable
    
        if executable is None:
            executable = args[0]
    
        sys.audit("subprocess.Popen", executable, args, cwd, env)
    
        if (_USE_POSIX_SPAWN
                and os.path.dirname(executable)
                and preexec_fn is None
                and not close_fds
                and not pass_fds
                and cwd is None
                and (p2cread == -1 or p2cread > 2)
                and (c2pwrite == -1 or c2pwrite > 2)
                and (errwrite == -1 or errwrite > 2)
                and not start_new_session
                and gid is None
                and gids is None
                and uid is None
                and umask < 0):
            self._posix_spawn(args, executable, env, restore_signals,
                              p2cread, p2cwrite,
                              c2pread, c2pwrite,
                              errread, errwrite)
            return
    
        orig_executable = executable
    
        # For transferring possible exec failure from child to parent.
        # Data format: "exception name:hex errno:description"
        # Pickle is not used; it is complex and involves memory allocation.
        errpipe_read, errpipe_write = os.pipe()
        # errpipe_write must not be in the standard io 0, 1, or 2 fd range.
        low_fds_to_close = []
        while errpipe_write < 3:
            low_fds_to_close.append(errpipe_write)
            errpipe_write = os.dup(errpipe_write)
        for low_fd in low_fds_to_close:
            os.close(low_fd)
        try:
            try:
                # We must avoid complex work that could involve
                # malloc or free in the child process to avoid
                # potential deadlocks, thus we do all this here.
                # and pass it to fork_exec()
    
                if env is not None:
                    env_list = []
                    for k, v in env.items():
                        k = os.fsencode(k)
                        if b'=' in k:
                            raise ValueError("illegal environment variable name")
                        env_list.append(k + b'=' + os.fsencode(v))
                else:
                    env_list = None  # Use execv instead of execve.
                executable = os.fsencode(executable)
                if os.path.dirname(executable):
                    executable_list = (executable,)
                else:
                    # This matches the behavior of os._execvpe().
                    executable_list = tuple(
                        os.path.join(os.fsencode(dir), executable)
                        for dir in os.get_exec_path(env))
                fds_to_keep = set(pass_fds)
                fds_to_keep.add(errpipe_write)
                self.pid = _posixsubprocess.fork_exec(
                        args, executable_list,
                        close_fds, tuple(sorted(map(int, fds_to_keep))),
                        cwd, env_list,
                        p2cread, p2cwrite, c2pread, c2pwrite,
                        errread, errwrite,
                        errpipe_read, errpipe_write,
                        restore_signals, start_new_session,
                        gid, gids, uid, umask,
                        preexec_fn)
                self._child_created = True
            finally:
                # be sure the FD is closed no matter what
                os.close(errpipe_write)
    
            self._close_pipe_fds(p2cread, p2cwrite,
                                 c2pread, c2pwrite,
                                 errread, errwrite)
    
            # Wait for exec to fail or succeed; possibly raising an
            # exception (limited in size)
            errpipe_data = bytearray()
            while True:
                part = os.read(errpipe_read, 50000)
                errpipe_data += part
                if not part or len(errpipe_data) > 50000:
                    break
        finally:
            # be sure the FD is closed no matter what
            os.close(errpipe_read)
    
        if errpipe_data:
            try:
                pid, sts = os.waitpid(self.pid, 0)
                if pid == self.pid:
                    self._handle_exitstatus(sts)
                else:
                    self.returncode = sys.maxsize
            except ChildProcessError:
                pass
    
            try:
                exception_name, hex_errno, err_msg = (
                        errpipe_data.split(b':', 2))
                # The encoding here should match the encoding
                # written in by the subprocess implementations
                # like _posixsubprocess
                err_msg = err_msg.decode()
            except ValueError:
                exception_name = b'SubprocessError'
                hex_errno = b'0'
                err_msg = 'Bad exception data from child: {!r}'.format(
                              bytes(errpipe_data))
            child_exception_type = getattr(
                    builtins, exception_name.decode('ascii'),
                    SubprocessError)
            if issubclass(child_exception_type, OSError) and hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = (err_msg == "noexec")
                if child_exec_never_called:
                    err_msg = ""
                    # The error must be from chdir(cwd).
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: PosixPath('dot')

/usr/lib/python3.10/subprocess.py:1863: FileNotFoundError

The above exception was the direct cause of the following exception:

graph = Graph(actions=[counter: count -> count], transitions=[Transition(from_=counter: count -> count, to=counter: count -> count, condition=condition: default)])
tmp_path = PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_3'), filename = 'app.png', write_dot = True

    @pytest.mark.parametrize(
        "filename, write_dot", [("app", False), ("app.png", False), ("app", True), ("app.png", True)]
    )
    def test_visualize_dot_output(graph, tmp_path: pathlib.Path, filename: str, write_dot: bool):
        """Handle file generation with `graph.Digraph` `.render()` and `.pipe()`"""
        output_file_path = f"{tmp_path}/{filename}"
    
>       graph.visualize(
            output_file_path=output_file_path,
            write_dot=write_dot,
        )

tests/core/test_graphviz_display.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/graph.py:211: in visualize
    _render_graphviz(
burr/core/graph.py:82: in _render_graphviz
    graphviz_obj.render(path_without_suffix, format=format, view=view)
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/rendering.py:122: in render
    rendered = self._render(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/backend/rendering.py:326: in render
    execute.run_check(cmd,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cmd = [PosixPath('dot'), '-Kdot', '-Tpng', '-O', 'app'], input_lines = None, encoding = None, quiet = False
kwargs = {'capture_output': True, 'cwd': PosixPath('/tmp/pytest-of-nduta/pytest-0/test_visualize_dot_output_app_3'), 'startupinfo': None}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
                proc = subprocess.run(cmd, **kwargs)
        except OSError as e:
            if e.errno == errno.ENOENT:
>               raise ExecutableNotFound(cmd) from e
E               graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:81: ExecutableNotFound
______________________________________________________________________________________________ test_echo_bot ______________________________________________________________________________________________

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f79580f90>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
>               proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:96: in _run_input_lines
    popen = subprocess.Popen(cmd, stdin=subprocess.PIPE, **kwargs)
/usr/lib/python3.10/subprocess.py:971: in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Popen: returncode: 255 args: [PosixPath('dot'), '-Kdot', '-Tpng']>, args = [PosixPath('dot'), '-Kdot', '-Tpng'], executable = b'dot', preexec_fn = None, close_fds = True, pass_fds = ()
cwd = None, env = None, startupinfo = None, creationflags = 0, shell = False, p2cread = 30, p2cwrite = 31, c2pread = 32, c2pwrite = 33, errread = 34, errwrite = 35, restore_signals = True, gid = None
gids = None, uid = None, umask = -1, start_new_session = False

    def _execute_child(self, args, executable, preexec_fn, close_fds,
                       pass_fds, cwd, env,
                       startupinfo, creationflags, shell,
                       p2cread, p2cwrite,
                       c2pread, c2pwrite,
                       errread, errwrite,
                       restore_signals,
                       gid, gids, uid, umask,
                       start_new_session):
        """Execute program (POSIX version)"""
    
        if isinstance(args, (str, bytes)):
            args = [args]
        elif isinstance(args, os.PathLike):
            if shell:
                raise TypeError('path-like args is not allowed when '
                                'shell is true')
            args = [args]
        else:
            args = list(args)
    
        if shell:
            # On Android the default shell is at '/system/bin/sh'.
            unix_shell = ('/system/bin/sh' if
                      hasattr(sys, 'getandroidapilevel') else '/bin/sh')
            args = [unix_shell, "-c"] + args
            if executable:
                args[0] = executable
    
        if executable is None:
            executable = args[0]
    
        sys.audit("subprocess.Popen", executable, args, cwd, env)
    
        if (_USE_POSIX_SPAWN
                and os.path.dirname(executable)
                and preexec_fn is None
                and not close_fds
                and not pass_fds
                and cwd is None
                and (p2cread == -1 or p2cread > 2)
                and (c2pwrite == -1 or c2pwrite > 2)
                and (errwrite == -1 or errwrite > 2)
                and not start_new_session
                and gid is None
                and gids is None
                and uid is None
                and umask < 0):
            self._posix_spawn(args, executable, env, restore_signals,
                              p2cread, p2cwrite,
                              c2pread, c2pwrite,
                              errread, errwrite)
            return
    
        orig_executable = executable
    
        # For transferring possible exec failure from child to parent.
        # Data format: "exception name:hex errno:description"
        # Pickle is not used; it is complex and involves memory allocation.
        errpipe_read, errpipe_write = os.pipe()
        # errpipe_write must not be in the standard io 0, 1, or 2 fd range.
        low_fds_to_close = []
        while errpipe_write < 3:
            low_fds_to_close.append(errpipe_write)
            errpipe_write = os.dup(errpipe_write)
        for low_fd in low_fds_to_close:
            os.close(low_fd)
        try:
            try:
                # We must avoid complex work that could involve
                # malloc or free in the child process to avoid
                # potential deadlocks, thus we do all this here.
                # and pass it to fork_exec()
    
                if env is not None:
                    env_list = []
                    for k, v in env.items():
                        k = os.fsencode(k)
                        if b'=' in k:
                            raise ValueError("illegal environment variable name")
                        env_list.append(k + b'=' + os.fsencode(v))
                else:
                    env_list = None  # Use execv instead of execve.
                executable = os.fsencode(executable)
                if os.path.dirname(executable):
                    executable_list = (executable,)
                else:
                    # This matches the behavior of os._execvpe().
                    executable_list = tuple(
                        os.path.join(os.fsencode(dir), executable)
                        for dir in os.get_exec_path(env))
                fds_to_keep = set(pass_fds)
                fds_to_keep.add(errpipe_write)
                self.pid = _posixsubprocess.fork_exec(
                        args, executable_list,
                        close_fds, tuple(sorted(map(int, fds_to_keep))),
                        cwd, env_list,
                        p2cread, p2cwrite, c2pread, c2pwrite,
                        errread, errwrite,
                        errpipe_read, errpipe_write,
                        restore_signals, start_new_session,
                        gid, gids, uid, umask,
                        preexec_fn)
                self._child_created = True
            finally:
                # be sure the FD is closed no matter what
                os.close(errpipe_write)
    
            self._close_pipe_fds(p2cread, p2cwrite,
                                 c2pread, c2pwrite,
                                 errread, errwrite)
    
            # Wait for exec to fail or succeed; possibly raising an
            # exception (limited in size)
            errpipe_data = bytearray()
            while True:
                part = os.read(errpipe_read, 50000)
                errpipe_data += part
                if not part or len(errpipe_data) > 50000:
                    break
        finally:
            # be sure the FD is closed no matter what
            os.close(errpipe_read)
    
        if errpipe_data:
            try:
                pid, sts = os.waitpid(self.pid, 0)
                if pid == self.pid:
                    self._handle_exitstatus(sts)
                else:
                    self.returncode = sys.maxsize
            except ChildProcessError:
                pass
    
            try:
                exception_name, hex_errno, err_msg = (
                        errpipe_data.split(b':', 2))
                # The encoding here should match the encoding
                # written in by the subprocess implementations
                # like _posixsubprocess
                err_msg = err_msg.decode()
            except ValueError:
                exception_name = b'SubprocessError'
                hex_errno = b'0'
                err_msg = 'Bad exception data from child: {!r}'.format(
                              bytes(errpipe_data))
            child_exception_type = getattr(
                    builtins, exception_name.decode('ascii'),
                    SubprocessError)
            if issubclass(child_exception_type, OSError) and hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = (err_msg == "noexec")
                if child_exec_never_called:
                    err_msg = ""
                    # The error must be from chdir(cwd).
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: PosixPath('dot')

/usr/lib/python3.10/subprocess.py:1863: FileNotFoundError

The above exception was the direct cause of the following exception:

    def test_echo_bot():
        @action(reads=["prompt"], writes=["response"])
        def echo(state: State) -> Tuple[dict, State]:
            return {"response": state["prompt"]}, state.update(response=state["prompt"])
    
        application = (
            ApplicationBuilder()
            .with_actions(
                prompt=Input("prompt"),
                response=echo,
            )
            .with_transitions(("prompt", "response"))
            .with_entrypoint("prompt")
            .build()
        )
        prompt = "hello"
        with patch("sys.stdin", new=StringIO(prompt)):
            run_action, result, state = application.run(
                halt_after=["response"], inputs={"prompt": input()}
            )
    
>       application.visualize(
            output_file_path="digraph",
            include_conditions=True,
            view=False,
            include_state=True,
            format="png",
        )

tests/test_end_to_end.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/application.py:1746: in visualize
    return self.graph.visualize(
burr/telemetry.py:276: in wrapped_fn
    return call_fn(*args, **kwargs)
burr/core/graph.py:211: in visualize
    _render_graphviz(
burr/core/graph.py:86: in _render_graphviz
    graphviz_obj.pipe(format=format)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:104: in pipe
    return self._pipe_legacy(format,
../burrenv_/lib/python3.10/site-packages/graphviz/_tools.py:171: in wrapper
    return func(*args, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:121: in _pipe_legacy
    return self._pipe_future(format,
../burrenv_/lib/python3.10/site-packages/graphviz/piping.py:161: in _pipe_future
    return self._pipe_lines(*args, input_encoding=self.encoding, **kwargs)
../burrenv_/lib/python3.10/site-packages/graphviz/backend/piping.py:161: in pipe_lines
    proc = execute.run_check(cmd, capture_output=True, quiet=quiet, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cmd = [PosixPath('dot'), '-Kdot', '-Tpng'], input_lines = <generator object pipe_lines.<locals>.<genexpr> at 0x7c3f79580f90>, encoding = None, quiet = False
kwargs = {'startupinfo': None, 'stderr': -1, 'stdout': -1}

    def run_check(cmd: typing.Sequence[typing.Union[os.PathLike, str]], *,
                  input_lines: typing.Optional[BytesOrStrIterator] = None,
                  encoding: typing.Optional[str] = None,
                  quiet: bool = False,
                  **kwargs) -> subprocess.CompletedProcess:
        """Run the command described by ``cmd``
            with ``check=True`` and return its completed process.
    
        Raises:
            CalledProcessError: if the returncode of the subprocess is non-zero.
        """
        log.debug('run %r', cmd)
        if not kwargs.pop('check', True):  # pragma: no cover
            raise NotImplementedError('check must be True or omited')
    
        if encoding is not None:
            kwargs['encoding'] = encoding
    
        kwargs.setdefault('startupinfo', _compat.get_startupinfo())
    
        try:
            if input_lines is not None:
                assert kwargs.get('input') is None
                assert iter(input_lines) is input_lines
                if kwargs.pop('capture_output'):
                    kwargs['stdout'] = kwargs['stderr'] = subprocess.PIPE
                proc = _run_input_lines(cmd, input_lines, kwargs=kwargs)
            else:
                proc = subprocess.run(cmd, **kwargs)
        except OSError as e:
            if e.errno == errno.ENOENT:
>               raise ExecutableNotFound(cmd) from e
E               graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH

../burrenv_/lib/python3.10/site-packages/graphviz/backend/execute.py:81: ExecutableNotFound
============================================================================================ warnings summary =============================================================================================
integration_tests/test_app.py::test_whole_application_tracker
  /home/nduta/burr_/burr/integrations/serde/langchain.py:35: LangChainBetaWarning: The function `load` is in beta. It is actively being worked on, so the API may change.
    return lc_serde.load(value)

integrations/test_burr_pydantic.py::test_subset_model_copy_config
  /home/nduta/burrenv_/lib/python3.10/site-packages/pydantic/_internal/_config.py:291: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.9/migration/
    warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)

tracking/test_local_tracking_client.py::test_application_tracks_end_to_end
  /home/nduta/burrenv_/lib/python3.10/site-packages/pydantic/main.py:1159: PydanticDeprecatedSince20: The `parse_obj` method is deprecated; use `model_validate` instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.9/migration/
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================================================= short test summary info =========================================================================================
FAILED tests/core/test_graphviz_display.py::test_visualize_dot_output[app-False] - graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH
FAILED tests/core/test_graphviz_display.py::test_visualize_dot_output[app.png-False] - graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH
FAILED tests/core/test_graphviz_display.py::test_visualize_dot_output[app-True] - graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH
FAILED tests/core/test_graphviz_display.py::test_visualize_dot_output[app.png-True] - graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH
FAILED tests/test_end_to_end.py::test_echo_bot - graphviz.backend.execute.ExecutableNotFound: failed to execute PosixPath('dot'), make sure the Graphviz executables are on your systems' PATH
========================================================================== 5 failed, 281 passed, 3 skipped, 3 warnings in 5.78s ================================