from deprecation import deprecated
from storage3 import SyncStorageClient,AsyncStorageClient
from storage3._sync.file_api import SyncBucketProxy
from storage3._async.file_api import AsyncBucketProxy


class SupabaseStorageClient(SyncStorageClient):
    """Manage storage buckets and files."""

    @deprecated("0.5.4", "0.6.0", details="Use `.from_()` instead")
    def StorageFileAPI(self, id_: str) -> SyncBucketProxy:
        return super().from_(id_)


class AsyncSupabaseStorageClient(AsyncStorageClient):
    """Manage storage buckets and files."""

    pass
